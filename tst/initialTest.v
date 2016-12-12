module initialTest;
   reg 			clk;
   reg 			rstn;
   reg 			RVld;
   reg [31:0] 	RData;
   wire        RRdy;
   wire [31:0] RAddr;
   
   initial begin
      clk = 0;
      forever begin
         #1 clk = !clk;
      end
   end

   initial begin
      rstn = 1;
      repeat (3) @(posedge clk);
      rstn <= 0;
      repeat (3) @(posedge clk);
      rstn <= 1;
   end

   initial begin
      repeat (1000) @(posedge clk);
      $finish;
   end

   initial begin
	   $dumpfile("sim.vcd");
	   $dumpvars(-1, dut);
   end

   lanzones dut(
      .clk(clk),
      .rstn(rstn),
      .RVld(RVld),
      .RData(RData),
      .RRdy(RRdy),
      .RAddr(RAddr));

   always @(posedge clk) begin
      if (rstn) begin
         RVld <= 0;
      end
      else begin
         if (RRdy) begin
            if (RVld) begin
               RVld <= 0;
            end
            else begin
               RVld <= 1;
            end
         end
      end
   end
endmodule
