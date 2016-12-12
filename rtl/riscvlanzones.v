module lanzones(
                input 			clk,
                input 			rstn,
                input 			RVld,
                input [31:0] 	RData,
                output 			RRdy,
                output [31:0]	RAddr
                );

   reg                 RRdy;
   reg [31:0]          RAddr;

   reg [31:0]          FIreg;
   reg [31:0]          DIreg;
   reg [31:0]          EXreg;
   reg [31:0]          MAreg;
   reg [31:0]          WBreg;

   wire                FIctrl;
   wire                DIctrl;
   wire                EXctrl;
   wire                MActrl;
   wire                WBctrl;

   assign FIctrl = 1;
   assign DIctrl = 1;
   assign EXctrl = 1;
   assign MActrl = 1;
   assign WBctrl = 1;

   always @(posedge clk) begin
      if (rstn) begin
         RRdy <= 0;
      end
      else begin
         if (RVld) begin
            RRdy <= 0;
         end
         else begin
            RRdy <= 1;
         end
      end
   end

   always @(posedge clk) begin
      if (rstn) begin
         FIreg <= 0;
      end
      else begin
         if (FIctrl) begin
            FIreg <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (rstn) begin
         DIreg <= 0;
      end
      else begin
         if (DIctrl) begin
            DIreg <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (rstn) begin
         EXreg <= 0;
      end
      else begin
         if (EXctrl) begin
            EXreg <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (rstn) begin
         MAreg <= 0;
      end
      else begin
         if (MActrl) begin
            MAreg <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (rstn) begin
         WBreg <= 0;
      end
      else begin
         if (WBctrl) begin
            WBreg <= 0;
         end
      end
   end
endmodule
