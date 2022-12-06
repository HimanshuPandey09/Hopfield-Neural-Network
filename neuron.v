`timescale 1ns / 1ps

module neuron #(weights = 25, 
                weightData = "weight_1.mif",
                ipnum = "testData.mif")(input clk,
                                        output reg NeuronOut);
               
// memory weight matrix is the weights for perticular neuron.
// ip is the input provided to the neuron for testing.  
// Both are given with .mif files.     
// Both have 25 entries each with 16 bit length.        
reg signed [15:0] memoryWeightMatrix [weights-1:0];
reg signed [15:0] ip [weights-1:0];
reg signed [33:0] weightedSum;

reg tempOut;

initial
    begin
        $readmemb(weightData, memoryWeightMatrix);
    end

initial
    begin
        $readmemb(ipnum, ip);
    end
    
always@(posedge clk)
    begin
        weightedSum <= ($signed(ip[0]) * $signed(memoryWeightMatrix[0])) + ($signed(ip[1]) * $signed(memoryWeightMatrix[1])) +
                       ($signed(ip[2]) * $signed(memoryWeightMatrix[2])) + ($signed(ip[3]) * $signed(memoryWeightMatrix[3])) +
                       ($signed(ip[4]) * $signed(memoryWeightMatrix[4])) + ($signed(ip[5]) * $signed(memoryWeightMatrix[5])) + 
                       ($signed(ip[6]) * $signed(memoryWeightMatrix[6])) + ($signed(ip[7]) * $signed(memoryWeightMatrix[7])) +
                       ($signed(ip[8]) * $signed(memoryWeightMatrix[8])) + ($signed(ip[9]) * $signed(memoryWeightMatrix[9])) + 
                       ($signed(ip[10]) * $signed(memoryWeightMatrix[10])) + ($signed(ip[11]) * $signed(memoryWeightMatrix[11])) +
                       ($signed(ip[12]) * $signed(memoryWeightMatrix[12])) + ($signed(ip[13]) * $signed(memoryWeightMatrix[13])) + 
                       ($signed(ip[14]) * $signed(memoryWeightMatrix[14])) + ($signed(ip[15]) * $signed(memoryWeightMatrix[15])) +
                       ($signed(ip[16]) * $signed(memoryWeightMatrix[16])) + ($signed(ip[17]) * $signed(memoryWeightMatrix[17])) + 
                       ($signed(ip[18]) * $signed(memoryWeightMatrix[18])) + ($signed(ip[19]) * $signed(memoryWeightMatrix[19])) + 
                       ($signed(ip[20]) * $signed(memoryWeightMatrix[20])) + ($signed(ip[21]) * $signed(memoryWeightMatrix[21])) + 
                       ($signed(ip[22]) * $signed(memoryWeightMatrix[22])) + ($signed(ip[23]) * $signed(memoryWeightMatrix[23])) + 
                       ($signed(ip[24]) * $signed(memoryWeightMatrix[24]));
    
    end

always @(posedge clk)
    begin
        if($signed(weightedSum)>=0)
            tempOut <= 1'b1;
 
        if($signed(weightedSum)<0)
            tempOut <= 1'b0;      
    end

always@(posedge clk)
    NeuronOut <= tempOut;
    


endmodule
