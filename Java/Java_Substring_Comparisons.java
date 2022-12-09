    public static String getSmallestAndLargest(String s, int k) {
        String curr_substr = s.substring(0, k);
        String smallest = curr_substr;
        String largest = curr_substr;

        for(int i = 0; i <= s.length()-k; i++){
            curr_substr = s.substring(i, i+k);
            
            if(curr_substr.compareTo(largest) > 0){
                largest = curr_substr;
            }

            if(curr_substr.compareTo(smallest) < 0){
                smallest = curr_substr;
            }
        }
        return smallest + "\n" + largest;
    }
