// A small example to help bring up compilation env of boost unit test.
// Used in boost-units.

#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE boost-unit-test
#include <boost/test/unit_test.hpp>

int add(int i, int j)
{
    return i + j;
}

BOOST_AUTO_TEST_CASE(universeInOrder)
{
    BOOST_CHECK(add(2, 2) == 4);
}
