# Hybrid String Matching Algorithm

This repository implements a hybrid string matching algorithm that combines the **Knuth-Morris-Pratt (KMP)** algorithm for exact matching, **Rabin-Karp** for efficient exact matching using hashing, and **Edit Distance** for approximate matching. It offers a powerful and efficient solution for analyzing and identifying patterns within large-scale datasets.

---

## **Features**
- Efficient **exact matching** using the KMP algorithm.
- Hash-based **exact matching** with **Rabin-Karp**, optimized for detecting patterns using rolling hashes.
- Flexible **approximate matching** within a user-specified tolerance using edit distance.
- Handles large files efficiently with chunk-based processing.

---

## **Getting Started**

### **Requirements**
This project is implemented in Python and requires Python 3.7 or higher. No additional dependencies are required (uses only Python's built-in libraries).

---

### **Setup**
1. Clone the repository:
   ```
   git clone https://github.com/festinam/StringMatching_KMP_EditDistance_GR22.git
   cd StringMatching_KMP_EditDistance_GR22
   ```

2. Run the script:
   ```
   python string_matching.py
   ```

---

## **Usage**
1. **Input the Pattern**: Provide the string pattern you want to search for.
2. **Set Tolerance**: Specify the tolerance level for approximate matching.
3. **Specify the File Path**: Enter the path to the text file where the pattern will be searched.
4. **View Results**: The script outputs all matches along with their types (exact via KMP, exact via Rabin-Karp, or approximate).

---

This project was completed by students from the Faculty of Electrical and Computer Engineering at the University of "Hasan Prishtina" under the expert guidance of Prof. Dr. Avni Rexhepi and Ass. Adrian Ymeri as part of the coursework in Design and Analysis of Algorithms.

## Authors
- [Elsa Vitija](https://github.com/elsavitija1)
- [Festina Mjeku](https://github.com/festinam)
- [Rina Halili](https://github.com/RinaHalili)
- [Vlera Islami](https://github.com/VleraIslami)