#include <iostream>
using namespace std;

class Solution {
public:
  bool solution(int x) {
    if (x) {
      return false;
    }
    return true;
  }
};

int main(int argc, char *argv[]) {
  Solution *solution = new Solution();
  bool result = solution->solution(0);
  cout << result;
  return 0;
}
