import holyapi

def main():
    print(f"""
Status       : {holyapi.status("status")}
Status Msg   : {holyapi.status("message")}

Info Message : {holyapi.info("infoMessage")}
Info Discord : {holyapi.info("discord")}
Info gh_org  : {holyapi.info("gh_organization")}
Info website : {holyapi.info("our_website")}
Info repo    : {holyapi.info("repository")}

Godsay (5)   : {holyapi.godsay(5)}

Quote (2)    :
{holyapi.quote(2)}

Divine Intel : {holyapi.divineintellect()}
Divine Msg   : {holyapi.divineintellect("message")}

Ask Terry    : {holyapi.askterry()}
""")

if __name__ == '__main__':
    main()
