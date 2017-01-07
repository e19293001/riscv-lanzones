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

   reg [31:0]          PCff;

   wire                FIctrl;
   reg                 DIctrlff;
   wire                EXctrl;
   wire                MActrl;
   wire                WBctrl;

   wire                PCctrl;

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
   reg [31:0]          xWData;
   reg 		 	        xWEn;

   reg                 stallctrl;

   assign FIctrl = (RRdy & RVld) ? 1 : 0;
   //assign DIctrl = 1;
   assign EXctrl = 1;
   assign MActrl = 1;
   assign WBctrl = 1;

   always @(posedge clk) begin
      if (!rstn) begin
         DIctrlff <= 0;
      end
      else begin
         if (FIctrl) begin
            DIctrlff <= 1;
         end
         else begin
            DIctrlff <= 0;
         end
      end
   end
   
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

   assign PCctrl = 1;
   
   always @(posedge clk) begin
      if (!rstn) begin
         PCff <= 0;
      end
      else begin
         if (LEn && RVld) begin
            if (PCctrl) begin
               PCff <= PCff + 1;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         RAddr <= 0;
      end
      else begin
         if (LEn) begin
            if (RVld) begin
               RAddr <= 0;
            end
            else begin
               RAddr <= PCff;
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

   wire [6:0]  opcode_instw;

   reg         DI_LUI_ctrl;
   reg [4:0]   rd_ctrl;
   reg [19:0]  imm_ctrl;

   reg         DI_ADD_ctrl;
   reg [6:0]   funct7_ctrl;
   reg [4:0]   rs1_ctrl;
   reg [4:0]   rs2_ctrl;
   reg [2:0]   funct3_ctrl;

   reg [31:0]  alu_outctrl;

   assign opcode_instw = FIff[6:0];

   always @* begin
      DI_LUI_ctrl = 0;
      DI_ADD_ctrl = 0;
      rd_ctrl = 0;
      imm_ctrl = 0;
      funct7_ctrl = 0;
      funct3_ctrl = 0;
      rs1_ctrl = 0;
      rs2_ctrl = 0;
      case (opcode_instw)
        7'b0110111: begin // LUI
           if (DIctrlff) begin
              DI_LUI_ctrl = 1;
              rd_ctrl = FIff[11:7];
              imm_ctrl = FIff[31:12];
           end
        end
        7'b0110011: begin // ADD
           if (DIctrlff) begin
              DI_ADD_ctrl = 1;
              funct7_ctrl = FIff[31:25];
              rs2_ctrl = FIff[24:20];
              rs1_ctrl = FIff[19:15];
              funct3_ctrl = FIff[14:12];
              rd_ctrl = FIff[11:7];
           end
        end
      endcase
   end

   always @* begin
      alu_outctrl = 0;
      if (DI_ADD_ctrl) begin
         alu_outctrl = rs1_ctrl + rs2_ctrl;
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         xWEn <= 0;
      end
      else begin
         if (DI_LUI_ctrl || DI_ADD_ctrl) begin
            xWEn <= 1;
         end
         else begin
            xWEn <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         xWData <= 0;
      end
      else begin
         if (DI_LUI_ctrl) begin
            xWData <= imm_ctrl;
         end
         else if (DI_ADD_ctrl) begin
            xWData <= alu_outctrl;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         xAddr <= 0;
      end
      else begin
         if (DI_LUI_ctrl) begin
            xAddr <= rd_ctrl;
         end
         else if (DI_ADD_ctrl) begin
            xAddr <= rd_ctrl;
         end
         else begin
            xAddr <= 0;
         end
      end
   end
 
   always @(posedge clk) begin
      if (!rstn) begin
         DIff <= 0;
      end
      else begin
         if (DIctrlff) begin
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
            EXff <= DIff;
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
   reg [31:0] xRData;
   always @* begin
      case (xAddr)
        0: xRData = x0ff;
        1: xRData = x1ff;
        2: xRData = x2ff;
        3: xRData = x3ff;
        4: xRData = x4ff;
        5: xRData = x5ff;
        6: xRData = x6ff;
        7: xRData = x7ff;
        8: xRData = x8ff;
        9: xRData = x9ff;
        10: xRData = x10ff;
        11: xRData = x11ff;
        12: xRData = x12ff;
        13: xRData = x13ff;
        14: xRData = x14ff;
        15: xRData = x15ff;
        16: xRData = x16ff;
        17: xRData = x17ff;
        18: xRData = x18ff;
        19: xRData = x19ff;
        20: xRData = x20ff;
        21: xRData = x21ff;
        22: xRData = x22ff;
        23: xRData = x23ff;
        24: xRData = x24ff;
        25: xRData = x25ff;
        26: xRData = x26ff;
        27: xRData = x27ff;
        28: xRData = x28ff;
        29: xRData = x29ff;
        30: xRData = x30ff;
        31: xRData = x31ff;
        default: xRData = 0;
      endcase
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x0ff <= 0;
      end
      else begin
         if (xAddr == 0) begin
            if (xWEn) begin
               x0ff <= xWData;
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
         end
      end
   end
endmodule
