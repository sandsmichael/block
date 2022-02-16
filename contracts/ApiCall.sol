pragma solidity >= 0.5.0 < 0.6.0; //

import "./Oraclize.sol"; //
//import "github.com/oraclize/ethereum-api/provableAPI.sol";

contract ApiCall is usingOraclize {

      uint public api_return_value;

      constructor() public {

            OAR = OraclizeAddrResolverI(0x371830767789f74d715CFD79157fa2331C5a9C18); 
      }

      function __callback(string memory result) public {
      if (msg.sender != oraclize_cbAddress()) revert();
            api_return_value = parseInt(result, 2); 
      }

      function query(string memory result) public payable {
            //oraclize_query("URL", html("https://www.wolframalpha.com/input?i2d=true&i=GOOGL+stock+price").xpath(//*[@id="__next"]/div/div[1]/main/div[2]/div/div[2]/section/section[2]/div/div/img/@alt); // helpers: html("").xpath; xml(); json();
            //oraclize_query("URL", "https://www.wolframalpha.com/input?i2d=true&i=GOOGL+stock+price");
            oraclize_query("WolframAlpha", "price of gasoline in Dallas * 1 gallon");
            //oraclize_query("WolframAlpha", json("https://www.therocktrading.com/api/ticker/BTCUSD".result.0.last));
            //oraclize_query("URL", "xml(https://www.fueleconomy.gov/ws/rest/fuelprices).fuelPrices.diesel"); 
      }

      function getOraclizePrice(string memory _datasource, uint _gasLimit) public payable returns (uint _dsprice){
          return oraclize_getPrice("URL", 80000);
     }

}