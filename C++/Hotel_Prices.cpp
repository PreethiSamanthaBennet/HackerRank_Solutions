#include <iostream>
#include <vector>

using namespace std;

class HotelRoom {
public:
    HotelRoom(int bedrooms, int bathrooms) 
    : bedrooms_(bedrooms), bathrooms_(bathrooms) {}

    virtual int get_price() {
        return 50*bedrooms_ + 100*bathrooms_;
    }

private:
    int bedrooms_;
    int bathrooms_;
};

class HotelApartment : public HotelRoom {

public:
    HotelApartment(int bedrooms, int bathrooms) 
    : HotelRoom(bedrooms, bathrooms) {}

    int get_price() {
        return HotelRoom::get_price() + 100;
    }
};
