try{
    const ascii = document.getElementById('ascii-input');

    // function
    ascii.addEventListener('input', function(){
        let binary_final_result = '';
        let decimal_final_result = "";
        let hex_final_result = "";
        // string 
        let string = ascii.value;

        // iterting 
        for (let i = 0; i < string.length; i++){

            // little string 
            let str = string[i].charCodeAt()

            // to bin 
            let placeholder = (Number(str).toString(2)).split("").reverse();
            // to decimal 
            decimal_final_result += (str + " ");
            // to hex
            hex_final_result += (str.toString(16) + " ")

            if (placeholder.length != 8){
                for (let i = 0; i < 8 - placeholder.length; i++){
                    placeholder.push("0")
                }
            }
            binary_final_result += placeholder.reverse().join("");
        }
        
        try{

            binary.value = binary_final_result;
            h2.textContent = binary_final_result;
        }
        catch (error){
            try{
                decimal.value = decimal_final_result;
                h2.textContent = decimal_final_result;
            }
            catch (error){
                hex.value = hex_final_result.toUpperCase();
                h2.textContent = hex_final_result.toUpperCase();
            }
        }
    });
}
catch (error){
    // do nothing
}