/* -*- c++ -*- */
/* 
 * Copyright 2013 Communications Engineering Lab (CEL) / Karlsruhe Institute of Technology (KIT)
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_LTE_BCH_CRC_CHECK_ANT_CHOOSER_BB_IMPL_H
#define INCLUDED_LTE_BCH_CRC_CHECK_ANT_CHOOSER_BB_IMPL_H

#include <gnuradio/lte/bch_crc_check_ant_chooser_bb.h>

namespace gr {
  namespace lte {

    class bch_crc_check_ant_chooser_bb_impl : public bch_crc_check_ant_chooser_bb
    {
     private:
      // Nothing to declare in this block.

     public:
      bch_crc_check_ant_chooser_bb_impl(std::string& name);
      ~bch_crc_check_ant_chooser_bb_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace lte
} // namespace gr

#endif /* INCLUDED_LTE_BCH_CRC_CHECK_ANT_CHOOSER_BB_IMPL_H */

