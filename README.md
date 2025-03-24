![initial image](images/image.webp)
-----------------------------
# 💻 PDA - Assignment 2 👾
## 📌 Student´s information:
- **Full names:** Andrés Felipe Vélez Alvarez - Sebastián Salazar Henao - Simón Mazo Gómez
- **Class number:** Monday SI2002-1 (7308)
------------------------------
# 🛠️ Development Environment:
- **Operating system:** macOS Sonoma 14.7.2
- **Programming language:** Python (interpreter version: Python 3.13.2)
- **Tools used:** Visual Studio Code, GitHub, Git, GitHub Desktop.

# 📖 About This Project

This project consists of the implementation of a **Pushdown Automaton (PDA)** capable of recognizing strings generated by a **Context-Free Grammar (CFG)**. It is divided into three main algorithms:

1. **String Generator:** Generates valid and invalid strings based on the grammar **S → aSb | ε**.
2. **Pushdown Automaton:** Simulates the PDA that determines whether the generated strings belong to the given grammar.
3. **[Pending Implementation]**

Each algorithm plays a crucial role in processing and verifying strings using formal language principles.

------------------------------
# 🚀 How to Run the Implementation:
### Prerequisites:
Ensure you have **Python 3.13.2** installed. You can check your version with:
```sh
python3 --version
```

### Running the Code:
1. Clone this repository:
```sh
git clone <https://github.com/EAFIT-AACS/assignment2-lfyc-group-2.git>
cd <the_folder_in_wich_you_saved_the_repository>
```

- It is highly suggested to run the algorithms in order, this is because algorithm 2 depends on algorithm 1, and algorithm 3 depends on algorithm 2.

2. Run the **first algorithm (string generator)**:
```sh
python ALGORITHM_1_LFC_2025_ASS.py
```
   - This will generate valid and invalid strings and save them in `String.txt` to implement the 2nd algorythm.

3. Run the **second algorithm (Pushdown Automaton (PDA) implementation)**:
```sh
python ALGORITHM_2_LFC_2025_ASS.py
```
   - This will read `String.txt`, process each string, and print whether it's **Accepted ✅** or **Rejected ❌** by the PDA. Then, the accepted strings will be saved in another txt for using the accepted string in the third algorythm.

4. Run the **third algorithm (processed configuration three of the PDA)**:
```sh
python ALGORITHM_3_LFC_2025_ASS.py
```
   - This will read `AcceptedString.txt` and will make a second verification of those strings. but also it is going to build the processed configuration tree for each string and it is going to show it in the console and in a .txt in order to make easy the procces of verification.
---
## ⚙️ Algorithm Explanation  

### 1️⃣ **Algorithm 1: String Generator**  
This algorithm generates strings based on the context-free grammar (CFG) rule:  
**S → aSb | ε**  

#### How it works:  
1. The user inputs the number of strings to generate for both valid and invalid cases (all in one number).  
2. The algorithm creates **valid** strings recursively following the CFG rule:  
   - A numer (n) its created randomly in a range of (0-10) that means the length of the string
   - If `n = 0`, return an empty string (ε).  
   - Otherwise, generate a string by adding an `"a"`, then recursively calling itself, and finally appending a `"b"`.  
   - Example: `n = 3` → `"aaabbb"`.  
3. **Invalid** strings are created randomly with characters `"a"` and `"b"` but force an incorrect structure (e.g., by adding an extra `"a"` at the end).  
4. Both valid and invalid strings are saved in a file named `String.txt`, which will be used in the next algorithm.  

#### Example Output:  
```plaintext
--- Strings: ---
aaabb
ab
aab
bbba
```  

### 2️⃣ **Algorithm 2: Pushdown Automaton (PDA)**  
This algorithm implements a **Pushdown Automaton (PDA)** based in the given grammar that processes the generated strings and determines whether they belong to the grammar.  

#### How it works:  
1. The PDA starts with an **initial state (`q0`)** and an **empty stack** initialized with `Z0` (bottom-of-stack marker).  
2. The PDA reads each character in the input string:  
   - If the character is `"a"`, it **pushes** `"A"` onto the stack.  
   - If the character is `"b"`, it **pops** `"A"` from the stack (only if there is an `"A"` available).  
   - If a `"b"` appears with no `"A"` to pop, the string is rejected.  
3. After processing all characters, the string is **accepted** if the stack only contains `Z0`. Otherwise, it is rejected.  
4. The PDA reads `String.txt`, processes each string, and prints whether it is **Accepted ✅** or **Rejected ❌**.  

#### Example Output:  
```plaintext
--- Processing Strings with PDA ---
String: aaabb -> Accepted ✅ by the PDA
String: ab -> Accepted ✅ by the PDA
String: aab -> Accepted ✅ by the PDA
String: bbba -> Rejected ❌ by the PDA
```  

---

### 3️⃣ **Algorithm 3: Processed Configuration Tree of the PDA**  
This algorithm takes the **accepted strings** from the previous PDA implementation and constructs a **configuration tree** for each one. The configuration tree visually represents the sequence of steps the PDA follows to process a given string.  

#### 🛠️ How it works:  
1. The algorithm reads **AcceptedStrings.txt**, which contains strings accepted by the PDA.  
2. Each string is processed again through the **Pushdown Automaton**, but this time, instead of only determining acceptance, it records every configuration change (state, remaining input, and stack contents).  
3. The configuration tree starts at the initial state (`q0`), displaying the full string and stack.  
4. As the PDA processes each character:  
   - `"a"` is read → `"A"` is pushed onto the stack.  
   - `"b"` is read → `"A"` is popped if available.  
   - Each step is recorded in the configuration tree.  
5. If the string is successfully processed and the stack is empty (except for `Z0`), the final configuration is stored with state `q_accept`.  
6. The configuration trees are displayed on the **console** and saved in `config_trees.txt` for easier verification.  

#### 📌 Example Output:  
For the accepted string `"aaabb"`:  

```plaintext
--- Generating Configuration Trees for Accepted Strings ---

String: aaabb

q0, aaabb, Z0  
q0, aabb, Z0A  
q0, abb, Z0AA  
q0, bb, Z0AAA  
q0, b, Z0AA  
q0, ε, Z0A  
q_accept, ε, Z0  
```

Processed configuration tree for: aaabb

### 📝 Explanation of Each Row  

Each row in the configuration tree represents a step in the PDA’s execution, consisting of:  

- **State**: The current state of the automaton (`q0` or `q_accept`).  
- **Remaining input**: The portion of the input string yet to be processed.  
- **Current stack contents**: The stack's state at that step.  

---

### 🎯 Purpose of This Algorithm  

✅ **Double-checks the correctness of accepted strings**  
✅ **Provides a structured visualization of PDA execution**  
✅ **Helps debug and verify context-free grammar adherence**  
---
