import speech_recognition as sr
import pyttsx3 
import httpx
from bs4 import BeautifulSoup


r = sr.Recognizer() 

def SpeakText(command):
 
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  
    engine.setProperty('rate', rate - 30) 
    engine.say(command)
    engine.runAndWait()
    

def get_comaand():
 while(1):    
 
    try:

        with sr.Microphone() as source2:
            
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            audio2 = r.listen(source2)
            
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            return MyText+'wikipedia'
            
    except sr.RequestError as e:
        print("Could not request results, {0}".format(e)) 
        
    except sr.UnknownValueError:
        print("nknown error occurred")


api_key = "Your API KEY"
search_engine_id = "Your Engine ID"

def google_first_result(query, api_key, cse_id):

    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": query,
        "num": 1,
    }

    response = httpx.get(search_url, params=params)
    response.raise_for_status()
    data = response.json()

    items = data.get("items")
    if not items:
        return "No results found."

    first = items[0]
    title = first.get("title", "No title")
    link = first.get("link", "No link")

    try:
        page_response = httpx.get(link, timeout=10)
        page_response.raise_for_status()
        soup = BeautifulSoup(page_response.text, "html.parser")
        
        paragraphs = soup.find_all("p")
        long_snippet = " ".join(p.get_text(strip=True) for p in paragraphs[:3])  

    except Exception as e:
        long_snippet = f"Could not fetch full content: {e}"

    SpeakText(f"{long_snippet}")


google_first_result(query=get_comaand(),api_key=api_key,cse_id=search_engine_id)

