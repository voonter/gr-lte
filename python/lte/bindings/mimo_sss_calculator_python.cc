/*
 * Copyright 2022 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

/***********************************************************************************/
/* This file is automatically generated using bindtool and can be manually edited  */
/* The following lines can be configured to regenerate this file during cmake      */
/* If manual edits are made, the following tags should be modified accordingly.    */
/* BINDTOOL_GEN_AUTOMATIC(0)                                                       */
/* BINDTOOL_USE_PYGCCXML(0)                                                        */
/* BINDTOOL_HEADER_FILE(mimo_sss_calculator.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(84cbf4dcab9f71d58c087aed4a09c97d)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/lte/mimo_sss_calculator.h>
// pydoc.h is automatically generated in the build directory
#include <mimo_sss_calculator_pydoc.h>

void bind_mimo_sss_calculator(py::module& m)
{

    using mimo_sss_calculator    = gr::lte::mimo_sss_calculator;


    py::class_<mimo_sss_calculator,
        gr::sync_block,
        gr::block,
        gr::basic_block,
        std::shared_ptr<mimo_sss_calculator>>(m, "mimo_sss_calculator", D(mimo_sss_calculator))

        .def(py::init(&mimo_sss_calculator::make),
           py::arg("rxant"),
           D(mimo_sss_calculator,make)
        )
        



        ;




}








