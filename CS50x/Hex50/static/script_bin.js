INT_NUM = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
HEX_NUM = {
    "0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9,
    "a" : 10,
    "b" : 11,
    "c" : 12,
    "d" : 13,
    "e" : 14,
    "f" : 15
}
const h2 = document.getElementById('ouput-everything')
try{
    const input_bin = document.getElementById('binary-input');

    // function for checking if the input os valid 
    function check(input_bin){
        let numbers = input_bin;
        for(let i = 0; i < numbers.length; i++){
            let number = numbers.charAt(i)
                if (number != "0" && number != "1"){
                    return false;
                }
        }
        return true;
    }

    // binary to hex
    const input_hex = document.getElementById('hex-output');

    input_bin.addEventListener('keyup', function(){
        let final_result = ""
        // checking if the input is valid
        if (check(input_bin.value) == false){
            input_dec = "";
            error_message.textContent = "invalid input";
            return;
        }
        // here is teh thing get the input from the user 
        // start eterating 
            // if the counter hits 4 start over 
            // but if you hit the end of the list aka i > list.lenght() puch what you got and break
        // use the last algorithm 

        // reversing the list 
        let reversed_numbers = input_bin.value.split("").reverse().join("");

        // counter and reult 
        let counter = 0;
        let index = 0
        let result = [0];

        // eteration 
        for (let i = 0; i < reversed_numbers.length; i++){
            let number = reversed_numbers.charAt(i);

            // doing the thing 
            result[index] += Number(number) * Math.pow(2, counter);
            counter ++;

            // checkin to resize 
            if (counter == 4){
                result.push(0);
                index++;
                counter = 0;
            }
        }
        // reversing result 
        result = result.reverse()

        // the last values 
        for (let i = 0; i < result.length; i++){
            let value = result[i];
            if (value in INT_NUM){
                final_result += INT_NUM[value]
            }
        }


        input_hex.value = final_result;
        h2.textContent = final_result;
    });


    // binary to decimal

    const input_dec = document.getElementById('dec-output');

    input_bin.addEventListener('keyup', function(){

        // checking if the number is valid
        if (check(input_bin.value) == false){
            input_dec = "";
            error_message.textContent = "invalid input";
            return ;
        }

        // reversing list 
        let reversed_numbers = input_bin.value.split("").reverse().join("");
        
        // math
        let counter = 0;

        // the final resault 
        let result = 0

        for (let i = 0; i < reversed_numbers.length; i++){
            let number = reversed_numbers.charAt(i);

            // claculating the result
            result += Number(number) * Math.pow(2, counter);
            counter ++;
        }
        input_dec.value = result;
        h2.textContent = result;
        error_message.textContent = "";
    });

    // binary to ascci
    const input_ascii = document.getElementById('ascii-output')

    input_bin.addEventListener('input', function(){
        // string or the input that is gonna be converted
        let string = input_bin.value;

        // checking 
        if (check(input_bin.value) == false || Number(string.length) % 8 != 0){
            return;
        }

        // counter 
        let counter = 0;

        // iteration time 
        let time = Math.floor(string.length / 8);

        // to stror the final resualt
        let ascii_string = "";

        for (let i = 0; i < time; i++){
            let result = 0;
            for (let j = 7; j > -1; j--){
                result += Number(string[counter]) * Math.pow(2, j);
                counter++;
            }
            ascii_string += String.fromCharCode(result);
        }
        // returning 
        input_ascii.value = ascii_string;
        h2.textContent = ascii_string;

    });

    // binary to unicode 

    let input_unicode = document.getElementById('unicode-output')

    input_bin.addEventListener('input', function(){

        // checking 


        // final result 
        let final_result = "";

        // getting the string 
        let string = [0]

        string = input_bin.value.split(" ");

        // iterating 
        for (let i = 0; i < string.length; i++){
            // setting counter 
            let counter = 0;
            let result = 0;

            // reversing the string 
            string[i] = string[i].split("").reverse().join("");

            // start iterating in every letter 
            for (let j = 0; j < string[i].length; j++){
                result += Number(string[i][j]) * Math.pow(2, counter);
                counter++;
            }
            final_result += String.fromCodePoint(result);
        }

        input_unicode.value = final_result;
        h2.textContent = final_result;

    });
    // done
}
catch (error){
    // do nothing 
}