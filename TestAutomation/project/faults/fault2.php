<?php #Destination: ./lib/maxmind/GeoIp2/Util.php

namespace GeoIp2;

class Util
{
    /**
     * This returns the network in CIDR notation for the given IP and prefix
     * length. This is for internal use only.
     *
     * @internal
     * @ignore
     *
     * @param mixed $ipAddress
     * @param mixed $prefixLen
     */
    public static function cidr($ipAddress, $prefixLen)
    {
        $ipBytes = inet_pton($ipAddress);
        $networkBytes = str_repeat("\0", \strlen($ipBytes));

        $curPrefix = $prefixLen;
        for ($i = 0; $i < \strlen($ipBytes)-1 && $curPrefix > 0; $i++) { // FAULT: Added -1
            $b = $ipBytes[$i];
            if ($curPrefix < 8) {
                $shiftN = 8 - $curPrefix;
                $b = \chr(0xFF & (\ord($b) >> $shiftN) << $shiftN);
            }
            $networkBytes[$i] = $b;
            $curPrefix -= 8;
        }

        $network = inet_ntop($networkBytes);

        return "$network/$prefixLen";
    }
}
