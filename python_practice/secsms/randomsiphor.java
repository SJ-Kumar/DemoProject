package TextBasedCipher;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.Random;

public class DChartCrypto
{
    private static String [][] CypherChart;
    private static int X_pos;
    private static int Y_pos;
    private static String Encrypted_Result;
    private static String Plaintext_Result;
    public static String[] Direction_Selected = new String[0];
    public static void main(String [] arg)
    {
        String Input=null;
        String Plaintext = new String();
        String [] CypherText = new String[0];
        StringBuilder CurrentCharacter = new StringBuilder();

        String[] Direction={"H", "V"};
        X_pos=0;
        Y_pos=0;

        //Cipher Chat
        CypherChart=
                new String[][]
                        {
                        {"."," ","0","1", "2", "3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"},
                        {"Z","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C"},
                        {"Y","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00"},
                        {"X","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01"},
                        {"W","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02"},
                        {"V","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03"},
                        {"U","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04"},
                        {"T","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05"},
                        {"S","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06"},
                        {"R","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07"},
                        {"Q","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08"},
                        {"P","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09"},
                        {"O","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A"},
                        {"N","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B"},
                        {"M","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C"},
                        {"L","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D"},
                        {"K","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E"},
                        {"J","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F"},
                        {"I","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A"},
                        {"H","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B"},
                        {"G","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C"},
                        {"F","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D"},
                        {"E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E"},
                        {"D","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F"},
                        {"C","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A"},
                        {"B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B"},
                        {"A","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C"},
                        {"9","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D"},
                        {"8","2F","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E"},
                        {"7","3A","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F"},
                        {"6","3B","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A"},
                        {"5","3C","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B"},
                        {"4","3D","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C"},
                        {"3","3E","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D"},
                        {"2","3F","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E"},
                        {"1","4A","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F"},
                        {"0","4B","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A"},
                        {" ","4C","00","01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F","1A","1B","1C","1D","1E","1F","2A","2B","2C","2D","2E","2F","3A","3B","3C","3D","3E","3F","4A","4B"},

                        };
        System.out.println("Chart Size: "+CypherChart.length);
        System.out.println("Please Enter your text:");
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        try {
            Input = in.readLine();
            Plaintext = Input.toUpperCase();
        }
        catch (Exception e)
        {
            System.out.println("Error "+e.getLocalizedMessage());
        }
        System.out.println("Plaintext: "+Input);
        Y_pos =1;
        X_pos =1;
        System.out.println(" ");
        Encrypted_Result =  Encrypt(Plaintext, Direction);
        System.out.println("The Encrypted Message is: "+Encrypted_Result);
        CypherText = Encrypted_Result.split(" ");
        Y_pos=1;
        X_pos=1;
        Plaintext_Result = Decrypt(CypherText,Direction_Selected);
        System.out.println("\nThe Decrypted message is: "+Plaintext_Result);
    }

    public static String Encrypt(String Plaintext, String [] Direction)
    {
        Direction_Selected = new String[Plaintext.length()];
        StringBuilder CurrentCharacter = new StringBuilder();
        for(int i=0;i<Plaintext.length();i++)
        {
            Random r=new Random();
            int randomNumber=r.nextInt(Direction.length);
            System.out.print(" "+Direction[randomNumber]);
            Direction_Selected[i]=Direction[randomNumber];
            if(Objects.equals(Direction[randomNumber], "H"))
            {
                CurrentCharacter.append(Encrypt_Horizontal(CypherChart, String.valueOf(Plaintext.charAt(i)),Y_pos));
            }
            else
            {
                CurrentCharacter.append(Encrypt_Vertical(CypherChart, String.valueOf(Plaintext.charAt(i)), X_pos));
            }
            CurrentCharacter.append(" ");
        }
        return CurrentCharacter.toString();
    }
    public static String Decrypt(String [] CipherText, String[] Direction_Selected)
    {
        StringBuilder CurrentCharacter = new StringBuilder();
        for (int c=0;c<CipherText.length;c++)
        {
            System.out.print(" "+Direction_Selected[c]);
            if(Direction_Selected[c].equals("H"))
            {
                CurrentCharacter.append(Decrypt_Horizontal(CypherChart, CipherText[c],Y_pos));
            }
            else
            {
                CurrentCharacter.append(Decrypt_Vertical(CypherChart, CipherText[c],X_pos));
            }
        }
        return CurrentCharacter.toString();
    }
    private static String Encrypt_Horizontal(String[][] InputChart, String Key, int Prev_Y)
    {
        String Temp=null;
        for(int i=0;i<CypherChart.length;i++)
        {
            if(InputChart[0][i].equals(Key))
            {
                X_pos =i;
                Y_pos=Prev_Y;
                Temp = InputChart[Y_pos][i];
                break;
            }
        }
        return Temp;
    }
    private static String Encrypt_Vertical(String[][] InputChart, String Key, int Prev_Y)
    {
        String Temp =null;
        for(int i=0;i<CypherChart.length;i++)
        {
            if(InputChart[i][0].equals(Key))
            {
                X_pos =Prev_Y;
                Y_pos=i;

                Temp = InputChart[i][X_pos];
                System.out.println(Temp);
                break;
            }
        }
        return Temp;
    }
    private static String Decrypt_Vertical(String[][] InputChart, String Key, int X)
    {
        String Temp=null;
        for(int i=0;i<CypherChart.length;i++)
        {
            if(InputChart[i][X].equals(Key))
            {
                X_pos =X;
                Y_pos=i;
                Temp =InputChart[i][0];
            }
        }
        return Temp;
    }
    private static String Decrypt_Horizontal(String[][] InputChart, String Key, int Y)
    {
        String Temp=null;
        for(int i=0;i<CypherChart.length;i++)
        {
            if(InputChart[Y][i].equals(Key))
            {
                X_pos =i;
                Y_pos=Y;
                Temp =InputChart[0][i];
            }
        }
        return Temp;
    }
}