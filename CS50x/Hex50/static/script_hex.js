HEX_NUM = {
    "0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9,
    "a" : 10,
    "b" : 11,
    "c" : 12,
    "d" : 13,
    "e" : 14,
    "f" : 15
}
try{
    // hex to binary
    const hex_input = document.getElementById('hex-input');


    // binary value 
    const binary_output = document.getElementById('bin-output');



    hex_input.addEventListener('input', function(){
        // getting the string 
        let string = hex_input.value;

        let decimal = parseInt(string, 16);

        let final_result = decimal.toString(2);

        binary_output.value = final_result;
        h2.textContent = final_result;
    });

    const dec_ouput = document.getElementById('dec-output');

    hex_input.addEventListener('input', function(){

        let string = hex_input.value;
        if (string == ""){
            dec_ouput.value = "0"
            h2.textContent = "0";
        }   
        else {
            let final_result = parseInt(string, 16);
        
            // setting the value 
            dec_ouput.value = final_result;
            h2.textContent = final_result;
        }
    });

    const ascii_output = document.getElementById('ascii-output'); 

    hex_input.addEventListener('input', function(){

        let string = hex_input.value.split(" ");

        let final_result = "";

        for (let i = 0; i < string.length; i++){

            let decimal = parseInt(string[i], 16);

            final_result += String.fromCharCode(decimal);
        }


        ascii_output.value = final_result;
        h2.textContent = final_result;
    });
    const unicode_input = document.getElementById('uni-output')
    hex_input.addEventListener('input', function(){
        let unicode_final_result = "";
        let string = hex_input.value;
        string = string.split(" ")

        console.log("hello");
        for (let i = 0; i < string.length; i++){
            let value = string[i];
            let decimal = parseInt(value, 16);
            unicode_final_result += String.fromCodePoint(decimal);     
        }
        console.log("hello2");
        
        unicode_input.value = string;
        h2.textContent = unicode_final_result;
    });
}
catch (error){
    // do nothing 
}