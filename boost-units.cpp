// Cannot "add" boost units quantities when they are "absolute"!

#include <iostream>  // for std::cout

#include <boost/units/quantity.hpp>
#include <boost/units/io.hpp>  // for quantities to be streamed to std::cout

// #include <boost/units/systems/si.hpp>
// #include <boost/units/systems/si/prefixes.hpp>
// #include <boost/units/systems/si/temperature.hpp>
#include <boost/units/systems/temperature/celsius.hpp>

#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE boost-units
#include <boost/test/unit_test.hpp>


/// Helper unit constants.
// vvv FAILS vvv
// static const auto celsius = boost::units::absolute<boost::units::celsius::temperature>();
// vvv WORKS vvv
static const auto celsius = boost::units::celsius::temperature();

BOOST_AUTO_TEST_CASE(temperatureAddition)
{
    auto temperature0 = 20.0 * celsius;
    auto temperature1 = 1.0 * celsius;
    auto temperature2 = temperature0 + temperature1;
    auto temperature3 = 21.0 * celsius;

    std::cout << "temperature2: " << temperature2 << std::endl;

    // vvv FAILS vvv
    // BOOST_CHECK_CLOSE(temperature2, temperature3, 1.0e-8);
    // vvv WORKS vvv
    BOOST_CHECK_CLOSE(temperature2 / celsius, temperature3 / celsius, 1.0e-4);

    // test increment
    auto temperature5 = temperature0 + 1 * celsius;
    BOOST_CHECK_CLOSE(temperature5 / celsius, 21.0, 1.0e-4);

    // test increment in loop
    double temperature_double = temperature0 / celsius;
    for (auto temperature = temperature0; temperature < 30.0 * celsius; temperature += 1.0 * celsius)
    {
        BOOST_CHECK_CLOSE(temperature / celsius, temperature_double, 1.0e-4);
        temperature_double += 1.0;
    }
}
