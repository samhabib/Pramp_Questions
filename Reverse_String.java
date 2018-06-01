 public static String reverse ( String arg ) {
    int str_len = arg.length();
    if(str_len < 2){
      return arg;
    }
    char[] char_array = arg.toCharArray();
    
    for(int i = 0; i < str_len / 2; i++){
        char temp = i;
        char_array[i] = char_array[str_len - (i + 1)];
        char_array[str_len - (i + 1)] = temp;
    }
    return new String(char_array);
 }
