`timescale 1ns / 1ps

module neuronTB #(weights = 25)();

reg clk;
wire NeuronOut;

neuron #(.weights(weights), .weightData("weight_1.mif"), .ipnum("testData1.mif")) n0(clk, NeuronOut);

initial
    begin
        clk = 1'b0;
//        rst=1'b1;
//		ctrl=1'b1;
end

//initial begin
//testdata[0] = 16'b0000000100000000;
//testdata[1] = 16'b0000000100000000;
//testdata[2] = 16'b0000000100000000;
//testdata[3] = 16'b0000000100000000;
//testdata[4] = 16'b0000000100000000;
//testdata[5] = 16'b1111111100000000;
//testdata[6] = 16'b1111111100000000;
//testdata[7] = 16'b1111111100000000;
//testdata[8] = 16'b1111111100000000;
//testdata[9] = 16'b0000000100000000;
//testdata[10] = 16'b1111111100000000;
//testdata[11] = 16'b1111111100000000;
//testdata[12] = 16'b1111111100000000;
//testdata[13] = 16'b1111111100000000;
//testdata[14] = 16'b0000000100000000;
//testdata[15] = 16'b1111111100000000;
//testdata[16] = 16'b1111111100000000;
//testdata[17] = 16'b1111111100000000;
//testdata[18] = 16'b1111111100000000;
//testdata[19] = 16'b0000000100000000;
//testdata[20] = 16'b0000000100000000;
//testdata[21] = 16'b0000000100000000;
//testdata[22] = 16'b0000000100000000;
//testdata[23] = 16'b0000000100000000;
//testdata[24] = 16'b0000000100000000;

//end

always
        #10 clk = ~clk;
        
initial 
 #1000 $finish;
endmodule
