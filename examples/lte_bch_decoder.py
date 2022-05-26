# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BCH Decoder
# Author: Johannes Demel
# Description: GR 3.7 hier block for LTE BCH decoding
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from gnuradio import lte







class lte_bch_decoder(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "BCH Decoder",
                gr.io_signature(1, 1, gr.sizeof_float*120),
                gr.io_signature.makev(2, 2, [gr.sizeof_char*24, gr.sizeof_char*1]),
        )

        ##################################################
        # Variables
        ##################################################
        self.final_xor4 = final_xor4 = 21845
        self.final_xor2 = final_xor2 = 65535
        self.final_xor1 = final_xor1 = 0
        self.data_len = data_len = 24

        ##################################################
        # Blocks
        ##################################################
        self.bch_vector_to_stream_3 = blocks.vector_to_stream(gr.sizeof_float*1, 40)
        self.bch_vector_to_stream_2 = blocks.vector_to_stream(gr.sizeof_float*1, 40)
        self.bch_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_float*1, 40)
        self.bch_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*40, 3)
        self.bch_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, 120)
        self.bch_stream_to_streams_0 = blocks.stream_to_streams(gr.sizeof_float*40, 3)
        self.bch_lte_subblock_deinterleaver_vfvf_2 = lte.subblock_deinterleaver_vfvf(40, 1, "$id")
        self.bch_lte_subblock_deinterleaver_vfvf_1 = lte.subblock_deinterleaver_vfvf(40, 1, "$id")
        self.bch_lte_subblock_deinterleaver_vfvf_0 = lte.subblock_deinterleaver_vfvf(40, 1, "$id")
        self.bch_lte_crc_check_vbvb_2 = lte.crc_check_vbvb(data_len, final_xor4, "$id")
        self.bch_lte_crc_check_vbvb_1 = lte.crc_check_vbvb(data_len, final_xor2, "$id")
        self.bch_lte_crc_check_vbvb_0 = lte.crc_check_vbvb(data_len, final_xor1, "$id")
        self.bch_lte_bch_viterbi_vfvb_0 = lte.bch_viterbi_vfvb()
        self.bch_lte_bch_crc_check_ant_chooser_bb_0 = lte.bch_crc_check_ant_chooser_bb("$id")
        self.bch_blocks_null_sink_1 = blocks.null_sink(gr.sizeof_char*data_len)
        self.bch_blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*data_len)
        self.bch_blocks_interleave_0 = blocks.interleave(gr.sizeof_float*1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.bch_blocks_interleave_0, 0), (self.bch_stream_to_vector_0, 0))
        self.connect((self.bch_lte_bch_crc_check_ant_chooser_bb_0, 0), (self, 1))
        self.connect((self.bch_lte_bch_viterbi_vfvb_0, 0), (self.bch_lte_crc_check_vbvb_0, 0))
        self.connect((self.bch_lte_bch_viterbi_vfvb_0, 0), (self.bch_lte_crc_check_vbvb_1, 0))
        self.connect((self.bch_lte_bch_viterbi_vfvb_0, 0), (self.bch_lte_crc_check_vbvb_2, 0))
        self.connect((self.bch_lte_crc_check_vbvb_0, 1), (self.bch_lte_bch_crc_check_ant_chooser_bb_0, 0))
        self.connect((self.bch_lte_crc_check_vbvb_0, 0), (self, 0))
        self.connect((self.bch_lte_crc_check_vbvb_1, 0), (self.bch_blocks_null_sink_0, 0))
        self.connect((self.bch_lte_crc_check_vbvb_1, 1), (self.bch_lte_bch_crc_check_ant_chooser_bb_0, 1))
        self.connect((self.bch_lte_crc_check_vbvb_2, 0), (self.bch_blocks_null_sink_1, 0))
        self.connect((self.bch_lte_crc_check_vbvb_2, 1), (self.bch_lte_bch_crc_check_ant_chooser_bb_0, 2))
        self.connect((self.bch_lte_subblock_deinterleaver_vfvf_0, 0), (self.bch_vector_to_stream_1, 0))
        self.connect((self.bch_lte_subblock_deinterleaver_vfvf_1, 0), (self.bch_vector_to_stream_2, 0))
        self.connect((self.bch_lte_subblock_deinterleaver_vfvf_2, 0), (self.bch_vector_to_stream_3, 0))
        self.connect((self.bch_stream_to_streams_0, 0), (self.bch_lte_subblock_deinterleaver_vfvf_0, 0))
        self.connect((self.bch_stream_to_streams_0, 1), (self.bch_lte_subblock_deinterleaver_vfvf_1, 0))
        self.connect((self.bch_stream_to_streams_0, 2), (self.bch_lte_subblock_deinterleaver_vfvf_2, 0))
        self.connect((self.bch_stream_to_vector_0, 0), (self.bch_lte_bch_viterbi_vfvb_0, 0))
        self.connect((self.bch_vector_to_stream_0, 0), (self.bch_stream_to_streams_0, 0))
        self.connect((self.bch_vector_to_stream_1, 0), (self.bch_blocks_interleave_0, 0))
        self.connect((self.bch_vector_to_stream_2, 0), (self.bch_blocks_interleave_0, 1))
        self.connect((self.bch_vector_to_stream_3, 0), (self.bch_blocks_interleave_0, 2))
        self.connect((self, 0), (self.bch_vector_to_stream_0, 0))


    def get_final_xor4(self):
        return self.final_xor4

    def set_final_xor4(self, final_xor4):
        self.final_xor4 = final_xor4

    def get_final_xor2(self):
        return self.final_xor2

    def set_final_xor2(self, final_xor2):
        self.final_xor2 = final_xor2

    def get_final_xor1(self):
        return self.final_xor1

    def set_final_xor1(self, final_xor1):
        self.final_xor1 = final_xor1

    def get_data_len(self):
        return self.data_len

    def set_data_len(self, data_len):
        self.data_len = data_len

