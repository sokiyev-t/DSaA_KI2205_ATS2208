from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'y'


def BSF_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    print(search_queue)
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is а mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False



BSF_search("you")
