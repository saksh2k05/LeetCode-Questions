class Solution {
public:
    string baseNeg2(int decnum){
        if (decnum==0) {
            return "0";
        }
        string res = "";

        while (decnum!= 0){
            int rem = decnum % -2;
            decnum = decnum/-2;
            if (rem < 0) {
                rem += 2;
                decnum++;
            }
            res = char(rem + '0') + res;
        }
        return res;
    }};
