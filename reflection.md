# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

When I first ran the game, it had a fairly simple UI and easy to navigate, however I've noticed a few bugs. First bug I noticed was that the hints were wrong. The game kept saying "Go Higher" after each guess despite the secret word being less and vise versa, it was saying "Go Lower" when my guess was lower than the secret. Second bug I noticed was the reset button didn't work. It reloaded a new secret key, but it didn't reset the game. Third bug I noticed was that the difficulties settings weren't working and the user can alter the text.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For this project I strictly used copilot. I described an error I was having with the games logic and it suggested that the logic error was coming from the check_guess function, where it was making incorrect comparisons. For the most part, copilot was extremly helpful and wasn't really misleading.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

In order to test out the bug fixes, I opened up the UI and tested the game to see if it gave me the desired output. I also used pytest to test the results to see if I got the right output for certain inputs. Ai helped me create these tests by walking me through each of the tests.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

For me, the main issue was that the game wouldn't reset, but the secret key did, but because a new game hasn't started, you weren't able to to guess the next secret key. Streamlit "reruns" is basically when streamlit re-executes your program from top to bottom everytime you interact with the UI. To give the game a stable secret key, I would save the current session state and reset it everytime the user clicks on "New Game"

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

In future projects, I would like to continue using a coding agent. I've realized that using a coding makes me more efficient and productive. The next time I use AI, I would like to refine my prompts to give it better instructions. AI generated code can be useful, but AI can make mistakes, so I've learned to use AI generated code responsibly.