# Serverless-Audio-Video-Chatbot

In simple terms, this project is like having a virtual assistant for students. People can upload their lecture audios or videos, and then chat about those files as if they were talking to a friend. OpenAI's Whisper transcribes those audios/videos and stores them in a persistent database. This becomes the knowledge base that people can ask questions about. It's like having a study buddy who never forgets anything from the lectures!

## Basic Streamlit App for demo

**Uploaded file:** 'Prompt Engineering of ChatGPT to Improve Generated Code & Runtime Performance Compared with the Top-Voted Human Solutions' Paper converted to audio using a Text-to-Speech service.

![Img](https://github.com/abhamidi-1234/Serverless-Audio-Video-Chatbot/blob/main/Streamlit%20App/Capture1.PNG)

**Question asked**: What is the name of the research paper? Who are the authors? What problems from Stack Overflow did they use? What prompting strategies did they use? Summarize the paper for me.

**Response from Chatbot:** 

*The name of the research paper is "Prompt Engineering of ChatGPT to Improve Generated Code and Runtime Performance Compared with the Top-Voted Human Solutions."*

*The authors of the paper are Ashraf Elnishar, Max Moundez, Douglas C. Schmidt, Jesse Spencer-Smith, and Jules White.*

*The paper presents the results of a study that compared the runtime performance of the best-performing coding solution generated with ChatGPT to the top-voted human-produced code on Stack Overflow. They selected 15 problems from Stack Overflow, which were grouped into two classes: one related to arrays and the other related to linked lists.*

*The problems from Stack Overflow that were used in the study include:*
*1. Identify missing numbers in an unsorted array.*
*2. Detect a duplicate number in an array that is not sorted.*
*3. Given an unsorted array, find the indices of the k smallest numbers.*
*4. Count pairs of elements in an array with a given sum.*
*5. Find duplicates in a list.*
*6. Remove list duplicates.*
*7. Implement the quicksort algorithm.*
*8. Reverse a list or iterate over it in reverse.*
*9. Count the frequency of elements in an unordered list.*
*10. Find the maximum product subarray.*
*11. Identify the middle element of a linked list in one traversal.*
*12. Detect if a linked list has a loop or cycle.*
*13. Reverse a linked list in Python.*
*14. Find the length of a linked list in Python.*
*15. Create Pascal's triangle in Python with a given number of rows.*

*Throughout the experiment, the authors applied various prompting strategies to generate Python code with ChatGPT. These prompting strategies include:*
*1. Naive Approach: Using the title from Stack Overflow as the prompt.*
*2. Ask for Speed Approach: Adding a requirement for speed at the end of the prompt.*
*3. Ask for Speed at Scale Approach: Providing more detailed information about optimizing the code for speed as the size of the list grows.*
*4. Ask for the Most Optimal Time Complexity: Prioritizing achieving the most optimal time complexity possible.*
*5. Ask for the Chain of Thought: Generating coherent text by providing a series of related prompts.*

*In summary, the paper concludes that selecting from the best of 100 solutions generated by ChatGPT is competitive or better than the top-voted human solution on Stack Overflow for the range of problems tested. The authors suggest that prompting multiple times for code and selecting the best of many generated solutions is a promising autonomous coding aid to help human software engineers find the best solutions for performance-critical code sections.*

