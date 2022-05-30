//SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.6.0 <0.9.0;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract RequestPrice is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    uint256 public price;

    address private oracle;
    bytes32 private jobId;
    uint256 private fee;
  

    /**
     * @notice Initialize the link token and target oracle
     *
     * Kovan Testnet details:
     * Link Token: 0xa36085F69e2889c224210F603D836748e7dC0088
     * Oracle: 0x74EcC8Bdeb76F2C6760eD2dc8A46ca5e581fA656 (Chainlink DevRel)
     * jobId: ca98366cc7314957b8c012c72f05aeeb
     *
     */
    constructor() {
        // setPublicChainlinkToken();
        oracle = 0x74EcC8Bdeb76F2C6760eD2dc8A46ca5e581fA656;
        jobId = "ca98366cc7314957b8c012c72f05aeeb";
        fee = 0.1 * 10 ** 18; 
    }

    /**
     * Create a Chainlink request to retrieve API response, find the target
     * data.
     */
    function requestPriceData() public returns (bytes32 requestId)
    {
        Chainlink.Request memory request = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);


        // Set the URL to perform the GET request on
        request.add("get", "https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsym=USD&e=Kraken");

        // Specify the path for retrieving the data
        request.add("path", "RAW.PRICE");
        // Sends the request
        return sendChainlinkRequestTo(oracle, request, fee);
    }

      /**
     * Callback Function
     */
    function fulfill(bytes32 _requestId, uint256 _price) public recordChainlinkFulfillment(_requestId)
    {
        price = _price;
    }
}