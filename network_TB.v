`timescale 1ns / 1ps
module network_TB #(weights = 25)();

reg clk;
wire [24:0]out;

network #(.weights(weights)) net(clk, out);

initial
    begin
        clk = 1'b0;
end

always
        #10 clk = ~clk;
        
initial 
 #1000 $finish;
endmodule
