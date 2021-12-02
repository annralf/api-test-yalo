import requests
from requests import exceptions

#Endpoints to consume
'''
https://jsonplaceholder.typicode.com/posts
https://jsonplaceholder.typicode.com/users
https://jsonplaceholder.typicode.com/posts/:postId/comments
'''

#Define CONS EP

postsList = "https://jsonplaceholder.typicode.com/posts"
usersList = "https://jsonplaceholder.typicode.com/users"
commentsList = "/comments"


#Test EP connection
apiConnTest = requests.get(usersList)

def getDataToProcess():
    data = []
    error  = None
    response = []
    try:
        postDataListRequest = requests.get(postsList) 
        usersDataListRequest = requests.get(usersList)
        postData = postDataListRequest.json()
        usersData = usersDataListRequest.json()
        data = {'posts': postData, 'users': usersData}        
    except requests.exceptions.ConnectionError as error:
        error = error
    response =  {'data': data, 'error': error}    
    return response        

def getUser(dataList, userId):
    if dataList['userId'] == userId:
        return dataList

def getUserPosts(postsList, userId):
    data = []
    error  = None
    response = []
    try:
        userPostList = filter(getUser(userId), postsList)
        data = userPostList
    except Exception as error:
        error = 'Error during pagination!' + error
    response =  {'data': data, 'error': error}    
    return response   

def getUserData(userList, userId):
    data = []
    error  = None
    response = []
    try:
        userList = filter(getUser(userId), userList)
        data = userList
    except Exception as e:
        error = error
    response =  {'data': data, 'error': error}    
    return response   
        
def getPaginate(postData, start, end):
    data = []
    error  = None
    response = []
    try:
        data = [ post for post in postData in range(start, end)]
    except:
        error = 'Error during pagination!'
    response =  {'data': data, 'error': error}    
    return response   



def getPostList(userId, start = None, end = None):
    data = {}
    error  = None
    response = []
    postsList = []
    try:
       dataToProcess = getDataToProcess()
       if dataToProcess['error']:
           error = dataToProcess['error']
       else:
           dataList = dataToProcess['data']
           postsUserList = getUserPosts(dataList['posts'], userId)
           if start and end:
               postsList = getDataToProcess(postsUserList, start, end)     
           else:
               postsList = postsUserList
           for posts in postsList:
              urlComments = postsList+'/'+postsList['id']+commentsList
              commentsListData = requests.get(urlComments)
              data['id'] = posts['id']   
              data['userId'] = posts['id']   
              data['title'] = posts['id']   
              data['body'] = posts['id']   
              data['user'] = postsUserList
              data['comments'] = commentsListData.json()
                     
    except Exception as e:
        error =  e
    response =  {'data': data, 'error': error}    
    return response     
    

print(getPostList(1))
