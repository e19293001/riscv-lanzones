module lanzones(
                input 			clk,
                input 			rstn,
                input 			RVld,
                input [31:0] 	RData,
                output 			RRdy,
                output [31:0]	RAddr,
                input         LEn
                );

   reg                 RRdy;
   reg [31:0]          RAddr;

   reg [31:0]          FIff;
   reg [31:0]          DIff;
   reg [31:0]          EXff;
   reg [31:0]          MAff;
   reg [31:0]          WBff;

   wire                FIctrl;
   wire                DIctrl;
   wire                EXctrl;
   wire                MActrl;
   wire                WBctrl;

   reg [31:0]          x0ff;
   reg [31:0]          x1ff;
   reg [31:0]          x2ff;
   reg [31:0]          x3ff;
   reg [31:0]          x4ff;
   reg [31:0]          x5ff;
   reg [31:0]          x6ff;
   reg [31:0]          x7ff;
   reg [31:0]          x8ff;
   reg [31:0]          x9ff;
   reg [31:0]          x10ff;
   reg [31:0]          x11ff;
   reg [31:0]          x12ff;
   reg [31:0]          x13ff;
   reg [31:0]          x14ff;
   reg [31:0]          x15ff;
   reg [31:0]          x16ff;
   reg [31:0]          x17ff;
   reg [31:0]          x18ff;
   reg [31:0]          x19ff;
   reg [31:0]          x20ff;
   reg [31:0]          x21ff;
   reg [31:0]          x22ff;
   reg [31:0]          x23ff;
   reg [31:0]          x24ff;
   reg [31:0]          x25ff;
   reg [31:0]          x26ff;
   reg [31:0]          x27ff;
   reg [31:0]          x28ff;
   reg [31:0]          x29ff;
   reg [31:0]          x30ff;
   reg [31:0]          x31ff;

   reg [4:0]           xAddr;
   reg [31:0]          xRData;
   reg [31:0]          xWData;
   reg 		 	        xWEn;

   always @(*) begin
      xWEn = 0;
      xAddr = 0;
      xRData = 0;
      xWData = 0;
   end

   assign FIctrl = (RRdy & RVld) ? 1 : 0;
   assign DIctrl = 1;
   assign EXctrl = 1;
   assign MActrl = 1;
   assign WBctrl = 1;

   always @(posedge clk) begin
      if (!rstn) begin
         RRdy <= 0;
      end
      else begin
         if (LEn) begin
            if (RVld) begin
               RRdy <= 0;
            end
            else begin
               RRdy <= 1;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         FIff <= 0;
      end
      else begin
         if (FIctrl) begin
            FIff <= RData;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         DIff <= 0;
      end
      else begin
         if (DIctrl) begin
            DIff <= FIff;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         EXff <= 0;
      end
      else begin
         if (EXctrl) begin
            EXff <= EXff;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         MAff <= 0;
      end
      else begin
         if (MActrl) begin
            MAff <= EXff;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         WBff <= 0;
      end
      else begin
         if (WBctrl) begin
            WBff <= MAff;
         end
      end
   end

// registers
   always @(posedge clk) begin
      if (!rstn) begin
         x0ff <= 0;
      end
      else begin
         if (xAddr == 0) begin
            if (xWEn) begin
               x0ff <= xWData;
            end
            else begin
               xRData <= x0ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x1ff <= 0;
      end
      else begin
         if (xAddr == 1) begin
            if (xWEn) begin
               x1ff <= xWData;
            end
            else begin
               xRData <= x1ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x2ff <= 0;
      end
      else begin
         if (xAddr == 2) begin
            if (xWEn) begin
               x2ff <= xWData;
            end
            else begin
               xRData <= x2ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x3ff <= 0;
      end
      else begin
         if (xAddr == 3) begin
            if (xWEn) begin
               x3ff <= xWData;
            end
            else begin
               xRData <= x3ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x4ff <= 0;
      end
      else begin
         if (xAddr == 4) begin
            if (xWEn) begin
               x4ff <= xWData;
            end
            else begin
               xRData <= x4ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x5ff <= 0;
      end
      else begin
         if (xAddr == 5) begin
            if (xWEn) begin
               x5ff <= xWData;
            end
            else begin
               xRData <= x5ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x6ff <= 0;
      end
      else begin
         if (xAddr == 6) begin
            if (xWEn) begin
               x6ff <= xWData;
            end
            else begin
               xRData <= x6ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x7ff <= 0;
      end
      else begin
         if (xAddr == 7) begin
            if (xWEn) begin
               x7ff <= xWData;
            end
            else begin
               xRData <= x7ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x8ff <= 0;
      end
      else begin
         if (xAddr == 8) begin
            if (xWEn) begin
               x8ff <= xWData;
            end
            else begin
               xRData <= x8ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x9ff <= 0;
      end
      else begin
         if (xAddr == 9) begin
            if (xWEn) begin
               x9ff <= xWData;
            end
            else begin
               xRData <= x9ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x10ff <= 0;
      end
      else begin
         if (xAddr == 10) begin
            if (xWEn) begin
               x10ff <= xWData;
            end
            else begin
               xRData <= x10ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x11ff <= 0;
      end
      else begin
         if (xAddr == 11) begin
            if (xWEn) begin
               x11ff <= xWData;
            end
            else begin
               xRData <= x11ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x12ff <= 0;
      end
      else begin
         if (xAddr == 12) begin
            if (xWEn) begin
               x12ff <= xWData;
            end
            else begin
               xRData <= x12ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x13ff <= 0;
      end
      else begin
         if (xAddr == 13) begin
            if (xWEn) begin
               x13ff <= xWData;
            end
            else begin
               xRData <= x13ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x14ff <= 0;
      end
      else begin
         if (xAddr == 14) begin
            if (xWEn) begin
               x14ff <= xWData;
            end
            else begin
               xRData <= x14ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x15ff <= 0;
      end
      else begin
         if (xAddr == 15) begin
            if (xWEn) begin
               x15ff <= xWData;
            end
            else begin
               xRData <= x15ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x16ff <= 0;
      end
      else begin
         if (xAddr == 16) begin
            if (xWEn) begin
               x16ff <= xWData;
            end
            else begin
               xRData <= x16ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x17ff <= 0;
      end
      else begin
         if (xAddr == 17) begin
            if (xWEn) begin
               x17ff <= xWData;
            end
            else begin
               xRData <= x17ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x18ff <= 0;
      end
      else begin
         if (xAddr == 18) begin
            if (xWEn) begin
               x18ff <= xWData;
            end
            else begin
               xRData <= x18ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x19ff <= 0;
      end
      else begin
         if (xAddr == 19) begin
            if (xWEn) begin
               x19ff <= xWData;
            end
            else begin
               xRData <= x19ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x20ff <= 0;
      end
      else begin
         if (xAddr == 20) begin
            if (xWEn) begin
               x20ff <= xWData;
            end
            else begin
               xRData <= x20ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x21ff <= 0;
      end
      else begin
         if (xAddr == 21) begin
            if (xWEn) begin
               x21ff <= xWData;
            end
            else begin
               xRData <= x21ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x22ff <= 0;
      end
      else begin
         if (xAddr == 22) begin
            if (xWEn) begin
               x22ff <= xWData;
            end
            else begin
               xRData <= x22ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x23ff <= 0;
      end
      else begin
         if (xAddr == 23) begin
            if (xWEn) begin
               x23ff <= xWData;
            end
            else begin
               xRData <= x23ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x24ff <= 0;
      end
      else begin
         if (xAddr == 24) begin
            if (xWEn) begin
               x24ff <= xWData;
            end
            else begin
               xRData <= x24ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x25ff <= 0;
      end
      else begin
         if (xAddr == 25) begin
            if (xWEn) begin
               x25ff <= xWData;
            end
            else begin
               xRData <= x25ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x26ff <= 0;
      end
      else begin
         if (xAddr == 26) begin
            if (xWEn) begin
               x26ff <= xWData;
            end
            else begin
               xRData <= x26ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x27ff <= 0;
      end
      else begin
         if (xAddr == 27) begin
            if (xWEn) begin
               x27ff <= xWData;
            end
            else begin
               xRData <= x27ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x28ff <= 0;
      end
      else begin
         if (xAddr == 28) begin
            if (xWEn) begin
               x28ff <= xWData;
            end
            else begin
               xRData <= x28ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x29ff <= 0;
      end
      else begin
         if (xAddr == 29) begin
            if (xWEn) begin
               x29ff <= xWData;
            end
            else begin
               xRData <= x29ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x30ff <= 0;
      end
      else begin
         if (xAddr == 30) begin
            if (xWEn) begin
               x30ff <= xWData;
            end
            else begin
               xRData <= x30ff;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x31ff <= 0;
      end
      else begin
         if (xAddr == 31) begin
            if (xWEn) begin
               x31ff <= xWData;
            end
            else begin
               xRData <= x31ff;
            end
         end
      end
   end
endmodule
