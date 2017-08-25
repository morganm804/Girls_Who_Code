class User:
    def __init__(self, user_name, user_id):
        self.user_name=user_name
        self.user_id=user_id
        self.connections=[]
    def addConnection(self, connection_id):
        self.connections.append(connection_id)
    def getUserName(self):
        return self.user_name
    def getConnections(self):
        return self.connections
    def getUserID(self):
        return self.user_id

class Network:
    def __init__(self):
        self.users=[]

    def numUsers(self):
        return len(self.users)

    def addUser(self,username):
        user_id=len(self.users)
        newUser=User(username, user_id)
        self.users.append(newUser)

    def getUserID(self,username):
        for person in self.users:
            if (person.getUserName()==username):
                return person.getUserID()

    def addConnection(self,user1,user2):
        user_id1=self.getUserID(user1)
        user_id2=self.getUserID(user2)
        user1.addConnection(user2)
        user2.addConnection(user1)

    # def displayConnections(self):
    #     for i in User.connections:
    #         print (User.getConnections())

def main():
    facebook=Network()
    username=input("What is your name?:")
    facebook.addUser(username)

    print(facebook.users[0].getUserName())
    print(facebook.users[0].getUserID())
main()
