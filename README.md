# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The game's purpose was to generate a secret key that the user had to guess. The user had to guess between a certain range of numbers and had limited guesses. If the user uses all of attempts before guessing the secret key then the user loses. The user can choose to turn on hits, so that after each guess the user will be notified to guess higher or lower. The first bug I noticed was that the hints were backwards. Everytime th user guessed a number lower than the scret key, then the game will tell you to guess lower. When you guess a higher number, the game would tell you to guess higher. I fixed this bug by changing the function responsible for this behavior and refactored the logic. The second bug I found was that the game wouldn't reset after pressing the button. I fixed this by clearing the session state of the game once the button has been pressed. Lastly, the last bug I encouter was that the diffulty wasn't properly applied. I fixed this by refactoring the function so that the game would refresh and apply the changes.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
      
<img width="706" height="579" alt="Screenshot" src="https://github.com/user-attachments/assets/4d0d0557-2d5a-4e51-b49f-06f0f7b77586" />


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
