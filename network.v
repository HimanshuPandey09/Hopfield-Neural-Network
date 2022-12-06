`timescale 1ns / 1ps

module network #(weights = 25)( input clk,
                                output reg [24:0]out);
                

wire [24:0] nextstate;


always @(posedge clk)       
    begin
        out <= nextstate;
    end         
    
    
neuron #(.weights(weights), .weightData("weight_1.mif"), .ipnum("testData.mif")) n0(.clk(clk), .NeuronOut(nextstate[0]));
neuron #(.weights(weights), .weightData("weight_2.mif"), .ipnum("testData.mif")) n1(.clk(clk), .NeuronOut(nextstate[1]));
neuron #(.weights(weights), .weightData("weight_3.mif"), .ipnum("testData.mif")) n2(.clk(clk), .NeuronOut(nextstate[2]));
neuron #(.weights(weights), .weightData("weight_4.mif"), .ipnum("testData.mif")) n3(.clk(clk), .NeuronOut(nextstate[3]));
neuron #(.weights(weights), .weightData("weight_5.mif"), .ipnum("testData.mif")) n4(.clk(clk), .NeuronOut(nextstate[4]));
neuron #(.weights(weights), .weightData("weight_6.mif"), .ipnum("testData.mif")) n5(.clk(clk), .NeuronOut(nextstate[5]));
neuron #(.weights(weights), .weightData("weight_7.mif"), .ipnum("testData.mif")) n6(.clk(clk), .NeuronOut(nextstate[6]));
neuron #(.weights(weights), .weightData("weight_8.mif"), .ipnum("testData.mif")) n7(.clk(clk), .NeuronOut(nextstate[7]));
neuron #(.weights(weights), .weightData("weight_9.mif"), .ipnum("testData.mif")) n8(.clk(clk), .NeuronOut(nextstate[8]));
neuron #(.weights(weights), .weightData("weight_10.mif"), .ipnum("testData.mif"))n9(.clk(clk), .NeuronOut(nextstate[9]));
neuron #(.weights(weights), .weightData("weight_11.mif"), .ipnum("testData.mif"))n10(.clk(clk), .NeuronOut(nextstate[10]));
neuron #(.weights(weights), .weightData("weight_12.mif"), .ipnum("testData.mif")) n11(.clk(clk), .NeuronOut(nextstate[11]));
neuron #(.weights(weights), .weightData("weight_13.mif"), .ipnum("testData.mif")) n12(.clk(clk), .NeuronOut(nextstate[12]));
neuron #(.weights(weights), .weightData("weight_14.mif"), .ipnum("testData.mif")) n13(.clk(clk), .NeuronOut(nextstate[13]));
neuron #(.weights(weights), .weightData("weight_15.mif"), .ipnum("testData.mif")) n14(.clk(clk), .NeuronOut(nextstate[14]));
neuron #(.weights(weights), .weightData("weight_16.mif"), .ipnum("testData.mif")) n15(.clk(clk), .NeuronOut(nextstate[15]));
neuron #(.weights(weights), .weightData("weight_17.mif"), .ipnum("testData.mif")) n16(.clk(clk), .NeuronOut(nextstate[16]));
neuron #(.weights(weights), .weightData("weight_18.mif"), .ipnum("testData.mif")) n17(.clk(clk), .NeuronOut(nextstate[17]));
neuron #(.weights(weights), .weightData("weight_19.mif"), .ipnum("testData.mif")) n18(.clk(clk), .NeuronOut(nextstate[18]));
neuron #(.weights(weights), .weightData("weight_20.mif"), .ipnum("testData.mif")) n19(.clk(clk), .NeuronOut(nextstate[19]));
neuron #(.weights(weights), .weightData("weight_21.mif"), .ipnum("testData.mif")) n20(.clk(clk), .NeuronOut(nextstate[20]));
neuron #(.weights(weights), .weightData("weight_22.mif"), .ipnum("testData.mif")) n21(.clk(clk), .NeuronOut(nextstate[21]));
neuron #(.weights(weights), .weightData("weight_23.mif"), .ipnum("testData.mif")) n22(.clk(clk), .NeuronOut(nextstate[22]));
neuron #(.weights(weights), .weightData("weight_24.mif"), .ipnum("testData.mif")) n23(.clk(clk), .NeuronOut(nextstate[23]));
neuron #(.weights(weights), .weightData("weight_25.mif"), .ipnum("testData.mif")) n24(.clk(clk), .NeuronOut(nextstate[24]));


endmodule
