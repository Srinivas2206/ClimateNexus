package main

import (
    "github.com/hyperledger/fabric-contract-api-go/contractapi"
)

type CarbonContract struct {
    contractapi.Contract
}

func (cc *CarbonContract) AddCredit(ctx contractapi.TransactionContextInterface, user string, credits int) error {
    return ctx.GetStub().PutState(user, []byte(strconv.Itoa(credits)))
}