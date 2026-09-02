 #include <string>
#include <vector>

class Solution {
public:
    std::string encode(const std::vector<std::string>& strs) {
        std::string encoded_string = "";
        
        for (const std::string& item : strs) {
            int item_length = item.length();

            encoded_string += std::to_string(item_length) + "#" + item;
        }
        
        return encoded_string;
    }


    std::vector<std::string> decode(const std::string& s) {
        std::vector<std::string> decoded_string;
        int i = 0;
        
        while (i < s.length()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            
            // std::stoi converts the string slice digits into a math integer
            // s.substr(i, j - i) gets the characters from position i to j
            int length = std::stoi(s.substr(i, j - i));
            
            int start = j + 1;
            
            // s.substr(start, length) grabs 'length' number of characters 
            // starting right after the '#' symbol
            std::string real_string = s.substr(start, length);
            
     
            decoded_string.push_back(real_string);
            
            // Move the index pointer to the start of the next block
            i = start + length;
        }
        
        return decoded_string;
    }
};
