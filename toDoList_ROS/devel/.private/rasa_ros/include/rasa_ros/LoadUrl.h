// Generated by gencpp from file rasa_ros/LoadUrl.msg
// DO NOT EDIT!


#ifndef RASA_ROS_MESSAGE_LOADURL_H
#define RASA_ROS_MESSAGE_LOADURL_H

#include <ros/service_traits.h>


#include <rasa_ros/LoadUrlRequest.h>
#include <rasa_ros/LoadUrlResponse.h>


namespace rasa_ros
{

struct LoadUrl
{

typedef LoadUrlRequest Request;
typedef LoadUrlResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct LoadUrl
} // namespace rasa_ros


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::rasa_ros::LoadUrl > {
  static const char* value()
  {
    return "5562f0f326dc984bc777bae8e1589603";
  }

  static const char* value(const ::rasa_ros::LoadUrl&) { return value(); }
};

template<>
struct DataType< ::rasa_ros::LoadUrl > {
  static const char* value()
  {
    return "rasa_ros/LoadUrl";
  }

  static const char* value(const ::rasa_ros::LoadUrl&) { return value(); }
};


// service_traits::MD5Sum< ::rasa_ros::LoadUrlRequest> should match
// service_traits::MD5Sum< ::rasa_ros::LoadUrl >
template<>
struct MD5Sum< ::rasa_ros::LoadUrlRequest>
{
  static const char* value()
  {
    return MD5Sum< ::rasa_ros::LoadUrl >::value();
  }
  static const char* value(const ::rasa_ros::LoadUrlRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::rasa_ros::LoadUrlRequest> should match
// service_traits::DataType< ::rasa_ros::LoadUrl >
template<>
struct DataType< ::rasa_ros::LoadUrlRequest>
{
  static const char* value()
  {
    return DataType< ::rasa_ros::LoadUrl >::value();
  }
  static const char* value(const ::rasa_ros::LoadUrlRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::rasa_ros::LoadUrlResponse> should match
// service_traits::MD5Sum< ::rasa_ros::LoadUrl >
template<>
struct MD5Sum< ::rasa_ros::LoadUrlResponse>
{
  static const char* value()
  {
    return MD5Sum< ::rasa_ros::LoadUrl >::value();
  }
  static const char* value(const ::rasa_ros::LoadUrlResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::rasa_ros::LoadUrlResponse> should match
// service_traits::DataType< ::rasa_ros::LoadUrl >
template<>
struct DataType< ::rasa_ros::LoadUrlResponse>
{
  static const char* value()
  {
    return DataType< ::rasa_ros::LoadUrl >::value();
  }
  static const char* value(const ::rasa_ros::LoadUrlResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // RASA_ROS_MESSAGE_LOADURL_H
