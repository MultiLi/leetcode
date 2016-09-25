char* reverseString(char* s) {
    int len = 0;
    while (s[len])  len++;
    int head = 0 , end = len - 1;
    int temp;
    while( end - head >= 1 + len % 2){
        temp = s[head];
        s[head] = s[end];
        s[end] = temp;
        end --;
        head ++;
    }

    return s;

}
