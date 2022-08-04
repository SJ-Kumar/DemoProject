import argparse
import os, sys
from enum import Enum
import weasyprint as wp
from jinja2 import Template
import urllib.parse
import requests
from io import BytesIO
from PIL import Image
from base64 import b64encode

class CertType(Enum):
    PARTICIPATION = "Participation"
    EXCELLENCE = "Excellence"

    def __str__(self):
        return self.value


class CertTemplate(Enum):
    BASIC = "basic"

    def __str__(self):
        return self.value

class Signature:
    def __init__(self, v):
        self.name, self.title, self.url = map(lambda x: x.strip(), v.split(","))

        try:
            if urllib.parse.urlparse(self.url).scheme in ('http', 'https',):
                r = requests.get(self.url)
                d = r.content
            else:
                with open(os.path.expanduser(self.url), "rb") as file:
                    d = file.read()
            
            buf = BytesIO()
            im = Image.open(BytesIO(d))
            im.save(buf, format="PNG")
            buf.seek(0)

            self.url = f"data:image/png;base64,{b64encode(buf.read()).decode()}"
        except Exception as e:
            print(f"Unable to get signature for {self.name}, {self.title}. [URL: {self.url}] (E: {e})")
            sys.exit(0)


def qr_code(args):
    return "https://chart.googleapis.com/chart?cht=qr&chs=100x100&chl=iitmbsc.org/?cid="+args
        

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Name of the certificated person", type=str, required=True)
parser.add_argument("-t", "--type", help="Type of the certificate", type=CertType, choices=list(CertType), default=CertType.PARTICIPATION)
parser.add_argument("-d", "--desc", "--description", help="Description/alt-text for the certificate", type=str)
parser.add_argument("-e", "--event", help="Event format: <name of the event>, <organizor>, <date of the event> (If desc was provided, it will be used instead)", type=str)
parser.add_argument("-s", "--signature", help='Signature format: "Title, Department, signature-png-file"', nargs='+', type=Signature, required=True)
parser.add_argument("-ct", "--cert-template", help="Template to use for making the certificate", type=CertTemplate, choices=list(CertTemplate), default=CertTemplate.BASIC)

args = parser.parse_args()

template = ""
try:
    with open(f"./template/{args.cert_template.value.strip('/')}/template.html", 'r') as file:
        template = file.read()
    
except Exception as e:
    print(f"Certificate Template doesn't exist. (E: {e})")
    sys.exit(0)

cert_desc = ""
if args.desc and args.desc.strip():
    cert_desc = cert_desc
else:
    if not args.event:
        print("Event must be specified if desc is not provided.")
        sys.exit(0)

    try:
        event_name, event_organizer, event_date = map(lambda x: x.strip(), args.event.split(","))
        match args.type:
            case CertType.PARTICIPATION:
                cert_desc = f"for participating in {event_name} held by {event_organizer} on {event_date}"

            case CertType.EXCELLENCE:
                cert_desc = f"for completing {event_name} held by {event_organizer} on {event_date}"
                
    except:
        print("Unable to set description for the certificate, check the event data provided.")
        sys.exit(0)

try:
    t = Template(template)
    template = t.render(cert_type=args.type.value, name=args.name.title(), cert_desc=cert_desc, signatures=args.signature, qr_code=qr_code(args))
except Exception as e:
    print(f"Unable to render certificate template. (E: {e})")
    sys.exit(0)

html = wp.HTML(string=template, base_url=f"./template/{args.cert_template.value.strip('/')}")
html.write_pdf(f"{args.name}.pdf")
