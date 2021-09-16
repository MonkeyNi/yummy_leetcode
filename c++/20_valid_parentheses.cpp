#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> parens;
        for (char& c : s) {
            switch (c) {
                case '(':
                case '{':
                case '[': parens.push(c); break;
                case ')': if (parens.empty() || parens.top() != '(') return false; else parens.pop(); break;
                case '}': if (parens.empty() || parens.top() != '{') return false; else parens.pop(); break;
                case ']': if (parens.empty() || parens.top() != '[') return false; else parens.pop(); break;
                default: ;
            }
        }
        return parens.empty()
    }

public:
    bool isValid2(string s) {
        stack<char> parens;
        for (const char& c : s) {
            switch (c) {
                case '(': parens.push(')'); break;
                case '{': parens.push('}'); break;
                case '[': parens.push(']'); break;
                default: 
                    if (parens.empty() || parens.top() != c) return false;
                    else parens.pop();
            }
        }
        return parens.empty();
    }
};