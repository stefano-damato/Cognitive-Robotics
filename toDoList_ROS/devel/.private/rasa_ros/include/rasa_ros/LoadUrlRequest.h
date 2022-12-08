// Generated by gencpp from file rasa_ros/LoadUrlRequest.msg
// DO NOT EDIT!


#ifndef RASA_ROS_MESSAGE_LOADURLREQUEST_H
#define RASA_ROS_MESSAGE_LOADURLREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rasa_ros
{
template <class ContainerAllocator>
struct LoadUrlRequest_
{
  typedef LoadUrlRequest_<ContainerAllocator> Type;

  LoadUrlRequest_()
    : url()  {
    }
  LoadUrlRequest_(const ContainerAllocator& _alloc)
    : url(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _url_type;
  _url_type url;





  typedef boost::shared_ptr< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> const> ConstPtr;

}; // struct LoadUrlRequest_

typedef ::rasa_ros::LoadUrlRequest_<std::allocator<void> > LoadUrlRequest;

typedef boost::shared_ptr< ::rasa_ros::LoadUrlRequest > LoadUrlRequestPtr;
typedef boost::shared_ptr< ::rasa_ros::LoadUrlRequest const> LoadUrlRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rasa_ros::LoadUrlRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rasa_ros::LoadUrlRequest_<ContainerAllocator1> & lhs, const ::rasa_ros::LoadUrlRequest_<ContainerAllocator2> & rhs)
{
  return lhs.url == rhs.url;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rasa_ros::LoadUrlRequest_<ContainerAllocator1> & lhs, const ::rasa_ros::LoadUrlRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rasa_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8b8fc5815211e556073b8281ccf07035";
  }

  static const char* value(const ::rasa_ros::LoadUrlRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8b8fc5815211e556ULL;
  static const uint64_t static_value2 = 0x073b8281ccf07035ULL;
};

template<class ContainerAllocator>
struct DataType< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rasa_ros/LoadUrlRequest";
  }

  static const char* value(const ::rasa_ros::LoadUrlRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string url\n"
;
  }

  static const char* value(const ::rasa_ros::LoadUrlRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.url);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LoadUrlRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rasa_ros::LoadUrlRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rasa_ros::LoadUrlRequest_<ContainerAllocator>& v)
  {
    s << indent << "url: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.url);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RASA_ROS_MESSAGE_LOADURLREQUEST_H
