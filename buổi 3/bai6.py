def findBigeerNumber(sampleArray):#khoi tao 1 ham findBigeerNumber co gia  tri la sampleArray
    biggestNumber= sampleArray[0]#gan gia tri cua sampleArray[0] = biggestNumber se mang gia tri đầu tiên của mảng sampleArray
    for index in range(1 ,len(sampleArray)):# khỏi tạo 1 vòng lặp for để lặp qua các giá trị của index và bắt đầu tại 1 kết thúc tại len(sampleArray)
        if sampleArray[index] > biggestNumber:# nếu sampleArray[index] > biggestNumber
            biggestNumber = sampleArray[index]#gan sampleArray[index] = biggestNumber thực hiện vòng lặp tang gia tri của index lên 1 và biggestNumber sẽ lưu giá cac gia tri do
    print(biggestNumber)# in ra gia tri cua biggestNumber