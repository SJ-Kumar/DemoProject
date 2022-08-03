#start code here
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random

namelist1 = pd.read_csv('./data/group1.csv')
namelist2 = pd.read_csv('./data/group2.csv')
namelist = pd.concat([namelist1, namelist2])

namelist.head()
namelist.tail()
print(len(namelist))


df = pd.read_csv("./data/friends_forever.csv", encoding= 'unicode_escape')
edge_list_temp_df = df[['Roll No', 'Edges']]

df.head()


edge_list_temp_df.head()


tempNodeList = df['Roll No'].values.tolist()
nodeList = list()
for node in tempNodeList:
  nodeList.append(node.strip().upper())

edgeList = edge_list_temp_df.values.tolist()
for edge in edgeList:
  nodes = edge[1].split(',')
  for node in nodes:
    if node.strip() != '':
      nodeList.append(node.strip().upper())


# Before removing Duplicate entry
print(len(nodeList))

# After removing Duplicate entry
nodeList = list(set(nodeList))
nodeList.sort()
print(len(nodeList))
print(nodeList)


def findName(roll):
  try:
    roll = roll.lower()
    res_df= namelist[namelist['Roll No']==roll]
    # print(roll, res_df)
    return str(res_df.iloc[0]['Name'])
  except:
    return roll


labels = []

for i in range(len(nodeList)):
  name = nodeList[i]
  labels.append(name)

nodeIds = [i+1 for i in range(len(nodeList))]
labelsTempDict = dict()
labelsDict = dict()

for i in range(len(labels)):
  labelsDict[nodeIds[i]] = labels[i]
  labelsTempDict[labels[i]] = nodeIds[i]


edge_list_df = pd.DataFrame(columns = ['Edge ID', 'Node 1', 'Node 2'])
i = 0
for edge in edgeList:
  nodes = edge[1].split(',')
  for node in nodes:
    if node.strip() != '':
      edge_list_df = edge_list_df.append({'Edge ID': i, 
                                          'Node 1' : labelsTempDict[edge[0].strip().upper()], 
                                          'Node 2' : labelsTempDict[node.strip().upper()]
                                          }, ignore_index = True)
      i += 1 
       
print(edge_list_df)


#process interests as list of strings
df.columns
df['Interests'] = list(map(lambda x: x.split(', '), df['Interests'].values.tolist()))
df['Languages'] = list(map(lambda x: x.split(', '), df['Languages'].values.tolist()))


df.head()


edgeList = edge_list_df.values.tolist()
G = nx.Graph()
G.add_nodes_from(nodeIds)
for i in range(len(edgeList)):
    G.add_edge(edgeList[i][1], edgeList[i][2])
# and we can easily retrieve the adjacency matrix 
AdjMatrix = nx.adjacency_matrix(G).A

nx.set_node_attributes(G, labels, "labels")


print(G.nodes())
print(G.edges())

nameDict = dict()
for key in labelsDict.keys():
  nameDict[key]=findName(labelsDict[key])


plt.figure(figsize=(25, 25))
nx.draw(G, with_labels=True, labels = nameDict)
plt.savefig("visualise.png")



## BFS Code
def bfsForNode(G, sourceNode):
  dp1 = set(sorted(list(nx.bfs_tree(G, source=sourceNode, depth_limit=1))))
  dp2 = set(sorted(list(nx.bfs_tree(G, source=sourceNode, depth_limit=2))))
  dp3 = set(sorted(list(nx.bfs_tree(G, source=sourceNode, depth_limit=3))))
  dp4 = set(sorted(list(nx.bfs_tree(G, source=sourceNode, depth_limit=4))))
  dp4 = dp4.difference(dp3)
  dp3 = dp3.difference(dp2)
  dp2 = dp2.difference(dp1)
  dp1 = dp1.difference(set([sourceNode]))
  # print([findName(labelsDict[x]) for x in dp1])
  # print('--------------')
  return dp1, dp2, dp3, dp4


def mutualFriendScore(G, sourceNode,dp1, dp2, dp3, dp4):   
    mutualScoreDict = dict()
    for node in dp2:
        dp1OfNode = set(sorted(list(nx.bfs_tree(G, source=node, depth_limit=1))))
        dp1OfNode = dp1OfNode.difference(set([node]))
        intersectionNodes = dp1OfNode.intersection(dp1)
        mutualScoreDict[node] = len(intersectionNodes)
    return mutualScoreDict


def calcInterestScore(sourceNode, depthList):
  sourceRollNo = labelsDict[sourceNode]
  tempInterestScoreDict = dict()
  for node in depthList:
      try:
        nodeRollNo = labelsDict[node]
        sourceNodeInterest = set(df.loc[df['Roll No'] == sourceRollNo]['Interests'].values.tolist()[0])
        nodeInterest = set(df.loc[df['Roll No'] == nodeRollNo]['Interests'].values.tolist()[0])
        intersections = sourceNodeInterest.intersection(nodeInterest)
        tempInterestScoreDict[node] = len(intersections)
      except:
        intersections = 0
        tempInterestScoreDict[node] = intersections
  return tempInterestScoreDict

def interestScore(sourceNode, dp1, dp2, dp3, dp4):   
  interestScoreDict = dict()
  interestScoreDict = calcInterestScore(sourceNode, dp2)
  interestScoreDict.update(calcInterestScore(sourceNode, dp3))
  interestScoreDict.update(calcInterestScore(sourceNode, dp4))

  return interestScoreDict

def calcLocationScore(sourceNode, depthList):
  sourceRollNo = labelsDict[sourceNode]
  sourceNodeDF = df[df['Roll No'] == sourceRollNo]
  tempLocScoreDict = dict()
  for node in depthList:
      try:
        sourceNodeLoc = str(sourceNodeDF.iloc[0]['City'])
        nodeRollNo = labelsDict[node]
        nodeDF = df[df['Roll No'] == nodeRollNo]
        nodeLoc = str(nodeDF.iloc[0]['City'])
        if sourceNodeLoc.strip().upper() == nodeLoc.strip().upper():
          tempLocScoreDict[node] = 1
        else:
          tempLocScoreDict[node] = 0
      except:
        tempLocScoreDict[node] = 0
  return tempLocScoreDict

def locationScore(sourceNode, dp1, dp2, dp3, dp4 ):
  locationScoreDict = dict()
  locationScoreDict = calcLocationScore(sourceNode, dp2)
  locationScoreDict.update(calcLocationScore(sourceNode, dp3))
  locationScoreDict.update(calcLocationScore(sourceNode, dp4))

  return locationScoreDict


def calcLanguageScore(sourceNode, depthList):
  sourceRollNo = labelsDict[sourceNode]
  tempLanguageScoreDict = dict()
  for node in depthList:
      try:
        nodeRollNo = labelsDict[node]
        sourceNodeLanguage = set(df.loc[df['Roll No'] == sourceRollNo]['Languages'].values.tolist()[0])
        nodeLanguage = set(df.loc[df['Roll No'] == nodeRollNo]['Languages'].values.tolist()[0])
        intersections = sourceNodeLanguage.intersection(nodeLanguage)
        tempLanguageScoreDict[node] = len(intersections)
      except:
        intersections = 0
        tempLanguageScoreDict[node] = intersections
  return tempLanguageScoreDict

def languageScore(sourceNode, dp1, dp2, dp3, dp4 ):
  languageScoreDict = dict()
  languageScoreDict = calcLanguageScore(sourceNode, dp2)
  languageScoreDict.update(calcLanguageScore(sourceNode, dp3))
  languageScoreDict.update(calcLanguageScore(sourceNode, dp4))

  return languageScoreDict


def printDictionary(friendList, dictionary):
  for node in friendList:
    print(findName(labelsDict[node]), dictionary[node])
  print('---'*30)

def finalSuggestion(dictionary, sourceRollNo, k, printBool = True):
  sortedRank = sorted(dictionary, key=dictionary.get, reverse=True)
  finalSuggestionList = sortedRank[:k] 
  friendEdgeList = list()
  for node in finalSuggestionList:
    friendEdgeList.append((labelsTempDict[sourceRollNo], node))
  # print(friendEdgeList)
  if printBool:
    printDictionary(finalSuggestionList, dictionary)
  return friendEdgeList

def friendSuggestionMain(graph, sourceRollNo, numberOfSuggestion, interestWeight = 5, 
                         languageWeight = 20, locationWeight = 30, mutualWeight = 80, printBool = True):
  sourceNode = labelsTempDict[sourceRollNo]
  dp1, dp2, dp3, dp4 = bfsForNode(graph, sourceNode)
  mutualFriendScoreDict = mutualFriendScore(graph, sourceNode, dp1, dp2, dp3, dp4)
  interestScoreDict = interestScore(sourceNode, dp1, dp2, dp3, dp4)
  languageScoreDict = languageScore(sourceNode, dp1, dp2, dp3, dp4)
  locationScoreDict = locationScore(sourceNode, dp1, dp2, dp3, dp4)

  mainScore = {}
  weights = [interestWeight, languageWeight, locationWeight, mutualWeight]
  depthFactors = [4, 3, 2]
  dicts = [interestScoreDict, languageScoreDict, locationScoreDict, mutualFriendScoreDict]
  for i in range(len(dicts)):
      
      for key, value in dicts[i].items():
        mainScore.setdefault(key, 0)
        
        # WITHOUT DEPTH FACTOR
        # mainScore[key] += weights[i]*value
  
        # WITH DEPTH FACTOR
        if i==len(dicts)-1:
          if key in dp2:
            mainScore[key] *= depthFactors[0]
          elif key in dp3:
            mainScore[key] *= depthFactors[1]
          elif key in dp4:
            mainScore[key] *= depthFactors[2]
          mainScore[key] += weights[i]*value
        else:
          mainScore[key] += weights[i]*value
 
  # Find the top n friends to be suggested
  if printBool:
    print("Suggestions for ", sourceRollNo, "-", findName(sourceRollNo))
  return finalSuggestion(mainScore, sourceRollNo, numberOfSuggestion, printBool)


dp1, dp2, dp3, dp4 = bfsForNode(G, labelsTempDict['21Z312'])
for node in G.nodes():
  G.nodes[node]["name"]=findName(labelsDict[node]) 
  if node in dp1:
    G.nodes[node]["depth"]=1
  if node in dp2:
    G.nodes[node]["depth"]=2
  if node in dp3:
    G.nodes[node]["depth"]=3
  if node in dp4:
    G.nodes[node]["depth"]=4
  ##nodeFriends = [j for i,j in finalFriendSuggestionDict['21Z312']]
  if node in nodeFriends:
    G.nodes[node]["depth"]=-1
nx.write_gml(G, "/Gephi Files/visualizeDeepthiFriends.gml")