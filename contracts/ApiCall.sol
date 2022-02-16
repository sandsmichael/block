pragma solidity >= 0.5.0 < 0.6.0; 

import "./Oraclize.sol";
//import "github.com/oraclize/ethereum-api/provableAPI.sol";

contract ApiCall is usingOraclize {

      uint public price;

      constructor() public {

            OAR = OraclizeAddrResolverI(0x371830767789f74d715CFD79157fa2331C5a9C18); 
      }

      function __callback(bytes32 myid, string memory result) public {
      if (msg.sender != oraclize_cbAddress()) revert();
            price = parseInt(result, 2); 
      }

      function query(bytes32 myid, string memory result) public payable {
            oraclize_query("URL", "https://www.wolframalpha.com/input?i2d=true&i=GOOGL+stock+price");
            //oraclize_query("WolframAlpha", "GOOGL stock price");
            //oraclize_query("URL", "xml(https://www.fueleconomy.gov/ws/rest/fuelprices).fuelPrices.diesel");
      }

}