pragma solidity ^0.8.11;

contract TodoList {

    uint public tasksCount  = 0; //  state variable --> these are written to the blockchain; represents the state of the contract; scope is global to contact; public enables us to read the var


    struct task{
        uint id;
        string description;
        bool completed;
    }
}

