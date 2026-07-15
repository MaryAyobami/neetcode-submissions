use std::collections::HashSet;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
    
    let set_array: HashSet<i32> = nums.iter().cloned().collect();

    if set_array.len() == nums.len() {
        return false;
    } else {
        return true;
    }
    }
}
