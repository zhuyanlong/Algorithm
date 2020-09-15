// 判断一个字符串按照字符串数组内的字符串分割，至少能分割成几段
// 给定字符串s，字符串数组dics，和字符串数组的长度n
package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        String s="aabbccdd";
        String[] dics=new String []{"aabb","cc","dd"};
        int n=4;
        int count=0;
        int i=0;
        int j=1;
        while(j!=s.length()+1){
            if(isHave(dics,s.substring(i,j))){
                count+=1;
                i=j;
                j=i+1;
            }
            else{
                j+=1;
            }
        }
        System.out.print(count);
    }
    public static boolean isHave(String[] strs,String s){
        int i;
        for(i=0;i< strs.length;i=i+1){
//          equals用来判断两个字符串的内容是否一样
            if(strs[i].equals(s)){
                return true;
            }
        }
        return false;
    }
}
