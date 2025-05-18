#include <iostream>
using namespace std;

class Solution {
public:
  bool isPalindrome(int x) {
    string y = to_string(x);
    size_t n = y.size();
    for (int i = 0; i < n / 2; i++) {
      if (y[i] != y[n - i - 1]) {
        return false;
      }
    }
    return true;
  }
};

int main(int argc, char *argv[]) {
  Solution *solution = new Solution();
  bool result = solution->isPalindrome(121);
  cout << result;
  return 0;
}
