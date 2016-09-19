// a xor b = b xor a, a xor a = 0, a xor 0 = a
// And a xor b xor c = (a xor b) xor c = a xor (b xor c)
// So finally the filtered one will be the single one

int singleNumber(int* nums, int numsSize) {

    int i;
    for(i = 1;i< numsSize;i++){
        nums[0] ^= nums[i];
    }

    return nums[0];
}
