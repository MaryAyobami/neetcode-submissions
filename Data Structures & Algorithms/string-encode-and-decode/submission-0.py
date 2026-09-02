class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for item in strs:
            item_length = len(item)
            encoded_string += f"{item_length}#{item}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []  
        i = 0
        
        while i < len(s):
            # Find where the '#' separator is
            j = i
            while s[j] != '#':
                j += 1
            
            # Read the length number before the '#'
            length = int(s[i:j])
            
            # Grab the exact text right after the '#' using slicing
            start = j + 1
            end = start + length
            real_string = s[start:end]
            
            # Save it 
            decoded_string.append(real_string)
            
            # Move our pointer 'i' to the next block of data
            i = end

        return decoded_string