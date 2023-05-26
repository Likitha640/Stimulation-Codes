#Harry & Sejal Conversation
import time

def person1():
    phrases = [
        "Hello!",
        "How are you?",
        "What have you been up to?",
        "That's interesting.",
        "I agree with you.",
        "It was nice talking to you. Goodbye!"
    ]
    
    for phrase in phrases:
        print("Harry:", phrase)
        time.sleep(2)
        
def person2():
    phrases = [
        "Hi there!",
        "I'm doing well, thanks.",
        "Just working on a project.",
        "Tell me more about your day.",
        "Glad to hear that.",
        "Goodbye! Take care!"
    ]
    
    for phrase in phrases:
        print(":", phrase)
        time.sleep(2)
        
def simulate_conversation():
    print("Initializing conversation...")
    time.sleep(1)
    
    print("Harry: Initiating conversation.")
    time.sleep(1)
    person1()
    
    print("\n Sejal : Responding to Harry.")
    time.sleep(1)
    person2()
    
    print("\nEnd of conversation.")
    
simulate_conversation()