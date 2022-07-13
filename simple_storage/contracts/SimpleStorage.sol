pragma solidity ^0.8.0;

contract SimpleStorage{

    uint256 favoriteNumber;
    bool favoriteBool;

    struct People {
        uint256 favoriteNumber;
        string name;
    }
    People[] public people;

    function store(uint256 _favoriteNumer) public returns(uint256){ 

        favoriteNumber = _favoriteNumer;

        return _favoriteNumer;
    }

    function retrieve() public view returns(uint256){
        return favoriteNumber;
    }
    function Addperson(string memory _name, uint256 _favoriteNumer)public{
        people.push(People( _favoriteNumer,_name));
    }
}