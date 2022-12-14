// Generated by gencpp from file rasa_ros/ExecuteJS.msg
// DO NOT EDIT!


#ifndef RASA_ROS_MESSAGE_EXECUTEJS_H
#define RASA_ROS_MESSAGE_EXECUTEJS_H

#include <ros/service_traits.h>


#include <rasa_ros/ExecuteJSRequest.h>
#include <rasa_ros/ExecuteJSResponse.h>


namespace rasa_ros
{

struct ExecuteJS
{

typedef ExecuteJSRequest Request;
typedef ExecuteJSResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ExecuteJS
} // namespace rasa_ros


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::rasa_ros::ExecuteJS > {
  static const char* value()
  {
    return "0bc1212ef5c5830fe8dbd8060c89a89d";
  }

  static const char* value(const ::rasa_ros::ExecuteJS&) { return value(); }
};

template<>
struct DataType< ::rasa_ros::ExecuteJS > {
  static const char* value()
  {
    return "rasa_ros/ExecuteJS";
  }

  static const char* value(const ::rasa_ros::ExecuteJS&) { return value(); }
};


// service_traits::MD5Sum< ::rasa_ros::ExecuteJSRequest> should match
// service_traits::MD5Sum< ::rasa_ros::ExecuteJS >
template<>
struct MD5Sum< ::rasa_ros::ExecuteJSRequest>
{
  static const char* value()
  {
    return MD5Sum< ::rasa_ros::ExecuteJS >::value();
  }
  static const char* value(const ::rasa_ros::ExecuteJSRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::rasa_ros::ExecuteJSRequest> should match
// service_traits::DataType< ::rasa_ros::ExecuteJS >
template<>
struct DataType< ::rasa_ros::ExecuteJSRequest>
{
  static const char* value()
  {
    return DataType< ::rasa_ros::ExecuteJS >::value();
  }
  static const char* value(const ::rasa_ros::ExecuteJSRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::rasa_ros::ExecuteJSResponse> should match
// service_traits::MD5Sum< ::rasa_ros::ExecuteJS >
template<>
struct MD5Sum< ::rasa_ros::ExecuteJSResponse>
{
  static const char* value()
  {
    return MD5Sum< ::rasa_ros::ExecuteJS >::value();
  }
  static const char* value(const ::rasa_ros::ExecuteJSResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::rasa_ros::ExecuteJSResponse> should match
// service_traits::DataType< ::rasa_ros::ExecuteJS >
template<>
struct DataType< ::rasa_ros::ExecuteJSResponse>
{
  static const char* value()
  {
    return DataType< ::rasa_ros::ExecuteJS >::value();
  }
  static const char* value(const ::rasa_ros::ExecuteJSResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // RASA_ROS_MESSAGE_EXECUTEJS_H
